#!/usr/bin/env python3
"""Validate content/projects.json and content/tracks.json parse and are
internally consistent:

  - both files are valid JSON
  - every project id is unique; ids match kind (w.. weekly, d.. daily)
  - every `concepts` entry names a real concept title from content/*.json
  - each project has the required fields and well-formed sub-shapes
  - weekly projects cover units 1..26 exactly once; rubric present and well-formed
  - every project referenced by a track exists
  - each track's schedule covers units 1..26, names a real weekly per unit,
    and lists only real daily-drill ids
  - est_hours carries all three track keys

Exit 0 = consistent. Exit 1 = any error.
"""
import json, os, glob, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")
ARTIFACT_KINDS = {"repo", "writeup", "benchmark", "photo", "paper-reproduction"}
EVIDENCE_OK = {"repo_url", "benchmark_output", "screenshot", "photo", "ci_run_url",
               "terminal_output", "paper_url"}
TRACK_KEYS = {"intensive", "sustained", "extended"}

errors = []
def err(where, msg): errors.append(f"ERROR  {where}: {msg}")


def real_titles():
    titles = set()
    for p in sorted(glob.glob(os.path.join(CONTENT, "[0-9]*.json"))):
        d = json.load(open(p))
        for s in d["sections"]:
            for c in s["concepts"]:
                titles.add(c["t"])
    return titles


def check_common(pw, p, titles, is_weekly):
    for k in ("id", "title", "domain_ids", "brief", "acceptance", "est_hours",
              "artifact_kind", "evidence_required", "concepts", "public_artifact"):
        if k not in p:
            err(pw, f"missing field '{k}'")
    if p.get("artifact_kind") not in ARTIFACT_KINDS:
        err(pw, f"bad artifact_kind {p.get('artifact_kind')!r}")
    for e in p.get("evidence_required", []):
        if e not in EVIDENCE_OK:
            err(pw, f"unknown evidence kind {e!r}")
    if not isinstance(p.get("acceptance"), list) or not p["acceptance"]:
        err(pw, "acceptance must be a non-empty list")
    else:
        for a in p["acceptance"]:
            if not a.get("id") or not a.get("text"):
                err(pw, "acceptance item missing id/text")
    eh = p.get("est_hours", {})
    if set(eh) != TRACK_KEYS:
        err(pw, f"est_hours must have keys {TRACK_KEYS}, got {set(eh)}")
    if not p.get("domain_ids"):
        err(pw, "domain_ids empty")
    if not isinstance(p.get("concepts"), list) or not p["concepts"]:
        err(pw, "concepts must be a non-empty list")
    else:
        seen = set()
        for t in p["concepts"]:
            if t in seen:
                err(pw, f"duplicate concept in list: {t!r}")
            seen.add(t)
            if t not in titles:
                err(pw, f"concepts entry not a real concept title: {t!r}")
    if len(p.get("brief", "")) < 150:
        err(pw, "brief is too short (want a real 200-500 word brief)")
    if is_weekly:
        if not re.match(r"^w\d\d-", p["id"]):
            err(pw, f"weekly id should look like w07-...: {p['id']!r}")
        rub = p.get("rubric")
        if not isinstance(rub, list) or not rub:
            err(pw, "weekly missing rubric")
        else:
            for r in rub:
                if not r.get("criterion") or "weight" not in r:
                    err(pw, "rubric row missing criterion/weight")
                lv = r.get("levels", {})
                if set(lv) < {"1", "3", "5"}:
                    err(pw, f"rubric levels must include 1,3,5: {r.get('criterion')!r}")
    else:
        if p.get("kind") != "daily":
            err(pw, "daily project missing kind=daily")
        if not re.match(r"^d\d\d-", p["id"]):
            err(pw, f"daily id should look like d07-3: {p['id']!r}")


def main():
    titles = real_titles()
    # ---- parse
    try:
        proj = json.load(open(os.path.join(CONTENT, "projects.json")))
    except Exception as e:
        print(f"ERROR  projects.json: not valid JSON — {e}"); return 1
    try:
        tracks = json.load(open(os.path.join(CONTENT, "tracks.json")))
    except Exception as e:
        print(f"ERROR  tracks.json: not valid JSON — {e}"); return 1

    weekly = proj.get("weekly", [])
    daily = proj.get("daily", [])
    all_ids = {}
    for p in weekly:
        check_common(f"weekly:{p.get('id')}", p, titles, True)
        all_ids[p["id"]] = all_ids.get(p["id"], 0) + 1
    for p in daily:
        check_common(f"daily:{p.get('id')}", p, titles, False)
        all_ids[p["id"]] = all_ids.get(p["id"], 0) + 1
    for pid, n in all_ids.items():
        if n > 1:
            err("projects", f"duplicate project id {pid!r} ({n}x)")

    # weekly covers units 1..26 exactly once
    wk_units = sorted(p.get("week") for p in weekly)
    if wk_units != list(range(1, 27)):
        err("weekly", f"weekly weeks must be exactly 1..26, got {wk_units}")
    proj_ids = set(all_ids)

    # ---- tracks
    if set(tracks.get("tracks", {})) != TRACK_KEYS:
        err("tracks", f"tracks must be {TRACK_KEYS}, got {set(tracks.get('tracks', {}))}")
    for key, t in tracks.get("tracks", {}).items():
        tw = f"track:{key}"
        sched = t.get("schedule", [])
        units = sorted(s.get("unit") for s in sched)
        if units != list(range(1, 27)):
            err(tw, f"schedule must cover units 1..26, got {units}")
        for s in sched:
            wp = s.get("weekly_project")
            if wp not in proj_ids:
                err(tw, f"unit {s.get('unit')} references missing project {wp!r}")
            for dd in s.get("daily_drills", []):
                if dd not in proj_ids:
                    err(tw, f"unit {s.get('unit')} references missing drill {dd!r}")
            for did in s.get("domains", []):
                pass  # domain ids are free-form focus labels
        # closure sanity
        c = t.get("closure", {})
        if not c.get("intake_closes"):
            err(tw, "intake does not close (rate * days < total concepts)")
        if not c.get("review_fits"):
            err(tw, "steady-state review load exceeds the review block")

    # every weekly must be referenced by every track's schedule
    for key, t in tracks.get("tracks", {}).items():
        referenced = {s["weekly_project"] for s in t.get("schedule", [])}
        missing = {p["id"] for p in weekly} - referenced
        if missing:
            err(f"track:{key}", f"weekly projects never scheduled: {sorted(missing)}")

    # every daily drill should be scheduled somewhere in each track
    for key, t in tracks.get("tracks", {}).items():
        referenced = set()
        for s in t.get("schedule", []):
            referenced.update(s.get("daily_drills", []))
        missing = {p["id"] for p in daily} - referenced
        if missing:
            err(f"track:{key}", f"daily drills never scheduled: {sorted(missing)[:6]} ...")

    for line in errors:
        print(line)
    print(f"\nprojects.json: {len(weekly)} weekly + {len(daily)} daily; "
          f"tracks.json: {len(tracks.get('tracks', {}))} tracks; "
          f"{len(errors)} errors.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
