#!/usr/bin/env python3
"""
Assign a stable `uid` to every domain, section, concept and L4 template that
does not already have one. Idempotent: existing uids are never touched.

    python3 build/assign_uids.py content/*.json          # fill what is missing
    python3 build/assign_uids.py --check content/*.json  # exit 1 if any are missing

Why this exists (PLAN-V2 §2.1): the importer used to identify a concept by
(section title, concept title) -- i.e. by where it sat in the file. Moving a
concept to another section or domain therefore archived the old row and
inserted a new one, orphaning every learner's FSRS history for it. The uid is
the identity; position is presentation.

uids are ULIDs (26 chars, Crockford base32, 48-bit ms timestamp + 80 random
bits): sortable, URL-safe, no collisions in practice, and generated ONCE here
and committed with the content. Never regenerate one.
"""
import json, os, secrets, sys, time

CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"


def ulid(ts_ms: int | None = None) -> str:
    ts = int(time.time() * 1000) if ts_ms is None else ts_ms
    rand = secrets.randbits(80)
    n = (ts << 80) | rand
    out = []
    for _ in range(26):
        out.append(CROCKFORD[n & 31])
        n >>= 5
    return "".join(reversed(out))


def is_ulid(s) -> bool:
    return isinstance(s, str) and len(s) == 26 and all(c in CROCKFORD for c in s)


def walk(doc, fill: bool):
    """Yield (path, has_uid) for every identity-bearing node; fill if asked."""
    d = doc.get("domain")
    if isinstance(d, dict):
        ok = is_ulid(d.get("uid"))
        if not ok and fill:
            d["uid"] = ulid(); ok = True
        yield ("domain", ok, d.get("uid"))
    for si, s in enumerate(doc.get("sections", [])):
        ok = is_ulid(s.get("uid"))
        if not ok and fill:
            s["uid"] = ulid(); ok = True
        yield (f"section[{si}] {s.get('t','?')}", ok, s.get("uid"))
        for ci, c in enumerate(s.get("concepts", [])):
            ok = is_ulid(c.get("uid"))
            if not ok and fill:
                c["uid"] = ulid(); ok = True
            yield (f"section[{si}].concept[{ci}] {c.get('t','?')}", ok, c.get("uid"))
            for ti, t in enumerate(c.get("L4") or []):
                if not isinstance(t, dict):
                    continue
                ok = is_ulid(t.get("uid"))
                if not ok and fill:
                    t["uid"] = ulid(); ok = True
                yield (f"section[{si}].concept[{ci}].L4[{ti}]", ok, t.get("uid"))


def main(argv):
    check = "--check" in argv
    files = [a for a in argv if not a.startswith("--")]
    if not files:
        print(__doc__); return 2
    missing = 0; filled = 0; seen = {}
    for f in files:
        with open(f, encoding="utf-8") as fh:
            doc = json.load(fh)
        before = sum(1 for _, ok, _ in walk(doc, fill=False) if not ok)
        for path, ok, uid in walk(doc, fill=not check):
            if not ok:
                missing += 1
                print(f"MISSING  {os.path.basename(f)} :: {path}")
            elif uid in seen:
                print(f"DUPLICATE uid {uid}: {seen[uid]} and {os.path.basename(f)} :: {path}")
                missing += 1
            else:
                seen[uid] = f"{os.path.basename(f)} :: {path}"
        if not check and before:
            with open(f, "w", encoding="utf-8") as fh:
                json.dump(doc, fh, ensure_ascii=False, indent=1)
                fh.write("\n")
            filled += before
            print(f"{os.path.basename(f)}: assigned {before} uids")
    if check:
        print(f"{len(seen)} uids, {missing} missing/duplicate")
        return 1 if missing else 0
    print(f"assigned {filled} uids; {len(seen)} total")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
