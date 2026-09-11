#!/usr/bin/env python3
"""
Corpus-level checks that no single-file validator can make.

    python3 build/validate_corpus.py            # content/[0-9]*.json
    python3 build/validate_corpus.py --report   # plus the v2 tier/resource coverage table

Exit 0 = the corpus is coherent. Exit 1 = a cross-file defect:

  1. uid uniqueness ACROSS files. build/validate_domain.py catches a duplicate
     within a file; a uid copied into another file is the defect that would
     make the importer treat two concepts as one.
  2. Preserved-topic survival ANYWHERE. The 408 source topics may move between
     files (v2 moves 139 Mathematics concepts to Level 0) but may never be
     lost, and their L1/L2 stay byte-identical to depthmap.json wherever they
     land. This replaces the per-file check for files that lose a topic to a
     move.
  3. Every L5 project ref names a project that exists in content/projects.json.
  4. Every qualified prereq (domain_id:Title) resolves to a live concept.

--report prints, per domain, how far the corpus is from the PLAN-V2 §1.4 tier
floors (>=3 tier-1, >=2 tier-2, >=2 tier-3 per concept) and the §5 resource
floors (>=2 structured resources, >=1 must). Those are targets for the audit
pass, not gates, so they never affect the exit code.
"""
import glob, json, os, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")


def load_source(path):
    """depthmap.json: [{title/sections/topics}] -> {topic title: [(d, m), ...]}"""
    src = json.load(open(path, encoding="utf-8"))
    out = defaultdict(list)
    for dom in src:
        for sec in dom.get("sections", []):
            for tp in sec.get("items", []):
                if isinstance(tp, dict):
                    out[tp.get("t")].append((tp.get("d", ""), tp.get("m", "")))
    return out


def main(argv):
    report = "--report" in argv
    files = sorted(glob.glob(os.path.join(CONTENT, "[0-9]*.json")))
    errors = []
    uids = {}
    concepts_by_dom = {}
    all_titles = defaultdict(set)     # domain_id -> titles
    preserved = []                    # (file, title, L1, L2)
    project_refs = []
    prereqs = []
    tier_stats = {}
    people_global = {}                # name -> (file, {x, site, verified, note})
    people_conflicts = []

    for f in files:
        name = os.path.basename(f)
        doc = json.load(open(f, encoding="utf-8"))
        dom = doc.get("domain", {})
        # 0. people are global; role/contribution are per domain (migration 011),
        #    but x / site / verified / note describe the person and must agree
        #    across files. A disagreement means at least one file is wrong.
        for person in doc.get("people", []) or []:
            pn = person.get("name")
            g = {k: person.get(k) for k in ("x", "site", "verified", "note")}
            if pn in people_global and people_global[pn][1] != g:
                pf, pg = people_global[pn]
                diff = {k: (pg[k], g[k]) for k in g if pg[k] != g[k]}
                people_conflicts.append((pn, pf, name, diff))
            people_global[pn] = (name, g)
        did = dom.get("id")
        nodes = [("domain", dom)]
        for si, s in enumerate(doc.get("sections", [])):
            nodes.append((f"sections[{si}]", s))
            for ci, c in enumerate(s.get("concepts", [])):
                w = f"sections[{si}].concepts[{ci}]"
                nodes.append((w, c))
                all_titles[did].add(c.get("t"))
                if c.get("preserved"):
                    preserved.append((name, c.get("t"), c.get("L1", ""), c.get("L2", "")))
                if isinstance(c.get("L5"), str):
                    project_refs.append((name, c["t"], c["L5"]))
                for p in c.get("prereqs", []) or []:
                    if ":" in p:
                        prereqs.append((name, c["t"], p))
                for ti, t in enumerate(c.get("L4") or []):
                    if isinstance(t, dict):
                        nodes.append((f"{w}.L4[{ti}]", t))
                # tier / resource coverage
                st = tier_stats.setdefault(name, Counter())
                st["concepts"] += 1
                tiers = Counter(int(t.get("tier", 1)) for t in (c.get("L4") or []) if isinstance(t, dict))
                st["t1_ok"] += tiers[1] >= 3
                st["t2_ok"] += tiers[2] >= 2
                st["t3_ok"] += tiers[3] >= 2
                res = c.get("resources") or []
                structured = [r for r in res if isinstance(r, dict)]
                st["res_ok"] += len(structured) >= 2 and any(r.get("priority") == "must" for r in structured)
        for w, node in nodes:
            u = node.get("uid") if isinstance(node, dict) else None
            if not isinstance(u, str):
                continue   # validate_domain.py reports missing/malformed
            if u in uids:
                errors.append(f"uid {u} appears in {uids[u]} AND {name} :: {w}")
            uids[u] = f"{name} :: {w}"

    # 2. preserved survival + byte-identity anywhere (if depthmap.json exists)
    depthmap_path = os.path.join(ROOT, "depthmap.json")
    if os.path.exists(depthmap_path):
        src = load_source(depthmap_path)
        seen_src = Counter()
        for name, title, l1, l2 in preserved:
            cands = src.get(title)
            if not cands:
                errors.append(f"{name}: '{title}' is marked preserved but is not a source topic")
                continue
            if not any(l1 == d and l2 == m for d, m in cands):
                errors.append(f"{name}: preserved '{title}' L1/L2 are not byte-identical to any source entry")
            seen_src[title] += 1
        missing = [t for t in src if seen_src[t] < len(src[t])]
        # Known, documented exception: the calculus 'Text' was renamed (BUILD-STATE §3).
        missing = [t for t in missing if not (t == "Text" and seen_src[t] == len(src[t]) - 1)]
        for t in missing:
            errors.append(f"source topic '{t}' ({len(src[t])} in source, {seen_src[t]} preserved in corpus) has been LOST — the curriculum may only grow")

    # 3. project refs
    pj = os.path.join(CONTENT, "projects.json")
    if os.path.exists(pj):
        p = json.load(open(pj, encoding="utf-8"))
        refs = {x.get("id") or x.get("ref") for k in ("weekly", "daily") for x in p.get(k, [])}
        for name, t, ref in project_refs:
            if ref not in refs:
                errors.append(f"{name}: '{t}' L5 names project ref {ref!r}, which is not in projects.json")

    # 4. qualified prereqs
    for name, t, p in prereqs:
        q, _, title = p.partition(":")
        if q in all_titles and title not in all_titles[q]:
            errors.append(f"{name}: '{t}' prereq {p!r} names a concept that does not exist in domain {q}")

    for e in errors:
        print("ERROR ", e)
    # Warnings, not errors: the corpus still ships, but the audit pass (PLAN-V2
    # §4.1 step C) has to settle each of these before "verified" means anything.
    for pn, a, b, diff in people_conflicts:
        keys = ", ".join(sorted(diff))
        print(f"WARN   person '{pn}' differs between {a} and {b} on {keys}")
    if people_conflicts:
        print(f"WARN   {len(people_conflicts)} cross-file people conflicts (x/site/verified/note); the later file wins on import")
    n_pres = len(preserved)
    src_str = f" (source {sum(len(v) for v in src.values())})" if 'src' in locals() and src is not None else ""
    print(f"\ncorpus: {len(files)} files, {len(uids)} uids, {sum(s['concepts'] for s in tier_stats.values())} concepts, "
          f"{n_pres} preserved{src_str}, {len(errors)} errors")

    if report:
        print("\nv2 coverage (PLAN-V2 §1.4 tier floors, §5 resource floor) — share of concepts meeting each:")
        print(f"{'file':32s} {'concepts':>8s} {'tier1>=3':>9s} {'tier2>=2':>9s} {'tier3>=2':>9s} {'res>=2+must':>12s}")
        tot = Counter()
        for name, st in tier_stats.items():
            n = st["concepts"]; tot.update(st)
            print(f"{name:32s} {n:8d} {st['t1_ok']/n:9.0%} {st['t2_ok']/n:9.0%} {st['t3_ok']/n:9.0%} {st['res_ok']/n:12.0%}")
        n = tot["concepts"]
        print(f"{'TOTAL':32s} {n:8d} {tot['t1_ok']/n:9.0%} {tot['t2_ok']/n:9.0%} {tot['t3_ok']/n:9.0%} {tot['res_ok']/n:12.0%}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
