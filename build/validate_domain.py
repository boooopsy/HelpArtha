#!/usr/bin/env python3
"""Validate a Whetstone domain content file against CONTENT-SPEC.md.

Usage: python3 build/validate_domain.py content/NN-slug.json [--source depthmap.json]
Exit 0 = clean. Exit 1 = errors. Warnings do not fail the build.
"""
import json, re, sys, os, argparse, math, itertools

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

KINDS = {"predict-output", "find-the-bug", "choose-and-justify", "compute",
         "derive", "explain", "security-review"}
GRADERS = {"exact", "numeric", "mcq", "cloze", "free", "code"}

# Unicode math that must be LaTeX instead
BANNED = "≤≥≠±×÷∞∑∏∫√∂∇αβγδεθλμσπρτφψωΣΠΔΩΘΛΦΨ⊗⊕∈∉⊂⊆∪∩∀∃¬∧∨→←↔⇒⇔≈≡∼⌊⌋⌈⌉‖·"
EMOJI = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]")

LEN = {"L1": (120, 320), "L2": (120, 330), "L3": (300, 900)}   # L3 ceiling 900 since 2026-09-10 (CONTENT-SPEC s3)

errors, warnings, todo = [], [], []


def err(where, msg):
    errors.append(f"ERROR  {where}: {msg}")


def warn(where, msg):
    warnings.append(f"WARN   {where}: {msg}")


def v2todo(where, msg):
    """Not a defect in the file as it stands: a v2 upgrade the audit pass owes
    it (PLAN-V2 §4.1). Counted separately so real warnings stay visible."""
    todo.append(f"TODO   {where}: {msg}")


def strip_code(s):
    """Remove fenced and inline code so banned-char checks ignore real source."""
    s = re.sub(r"```.*?```", "", s, flags=re.S)
    s = re.sub(r"`[^`]*`", "", s)
    return s


def strip_math(s):
    """Remove $...$ and $$...$$ so we only scan prose."""
    s = re.sub(r"\$\$.*?\$\$", "", s, flags=re.S)
    s = re.sub(r"\$[^$]*\$", "", s)
    return s


QUALIFIED = re.compile(r"^([A-Za-z0-9_]{1,16}):(\S.*)$")


def domain_qualifiers(content_dir=None):
    """Every legal prereq qualifier: each domain's `id` and its two-digit `n`.

    Kept as an allowlist because concept titles routinely contain a colon
    ("Pagination: offset, keyset, cursor"), so the shape of the string is not
    enough to tell a qualifier from a subtitle.
    """
    import glob
    cd = content_dir or os.path.join(ROOT, "content")
    quals = set()
    for f in glob.glob(os.path.join(cd, "[0-9][0-9]*-*.json")):
        try:
            dom = json.load(open(f)).get("domain") or {}
        except Exception:
            continue
        quals.update(x for x in (dom.get("id"), dom.get("n")) if x)
    return quals


QUALS = domain_qualifiers()


def split_prereq(p):
    """Split a prereq reference into (qualifier, title).

    A prereq is either a bare "Concept Title" (resolved by title across the
    whole corpus) or a qualified "domain_id:Concept Title" — CONTENT-SPEC §3.
    The qualifier is the target domain's `id` (e.g. `arch`) or its two-digit
    `n` (e.g. `04`), with no space after the colon. Qualification is required
    whenever the bare title is ambiguous, i.e. carried by a concept in more
    than one domain. Anything whose prefix is not a real domain qualifier is a
    plain title, colons and all.
    """
    m = QUALIFIED.match(p or "")
    if not m or m.group(1) not in QUALS:
        return None, p
    return m.group(1), m.group(2)


ULID = re.compile(r"^[0-9A-HJKMNP-TV-Z]{26}$")
RESOURCE_KINDS = {"lecture", "notes", "paper", "book", "lab", "doc", "video", "tool", "post", "repo"}
RESOURCE_PRIORITIES = {"must", "important", "optional"}
_seen_uids = {}


def check_uid(where, node):
    """PLAN-V2 §2.1: every domain, section, concept and L4 template carries a
    ULID that is its identity. Missing is an error here (this is the corpus
    gate; run build/assign_uids.py). Duplicates within a file are caught here;
    across files by build/validate_corpus.py."""
    u = node.get("uid") if isinstance(node, dict) else None
    if u is None:
        err(where, "missing uid — run build/assign_uids.py")
        return
    if not isinstance(u, str) or not ULID.fullmatch(u):
        err(where, f"uid {u!r} is not a 26-char Crockford-base32 ULID")
        return
    if u in _seen_uids:
        err(where, f"uid {u} duplicates {_seen_uids[u]} — a uid is never reused")
    _seen_uids[u] = where


def check_resource(where, r):
    """PLAN-V2 §5: a bare https URL (legacy, warns) or a structured object."""
    if isinstance(r, str):
        if not r.startswith("https://"):
            err(where, f"resource not https: {r}")
        else:
            v2todo(where, "bare-URL resource; v2 wants {url,title,kind,priority,why}")
        return
    if not isinstance(r, dict):
        err(where, "resource must be a URL string or an object"); return
    u = r.get("url")
    if not isinstance(u, str) or not u.startswith("https://"):
        err(where, f"resource.url not https: {u!r}")
    if not r.get("title"):
        warn(where, "resource has no title")
    if r.get("kind") not in RESOURCE_KINDS:
        err(where, f"resource.kind {r.get('kind')!r} not in {sorted(RESOURCE_KINDS)}")
    if r.get("priority") not in RESOURCE_PRIORITIES:
        err(where, f"resource.priority {r.get('priority')!r} not in must|important|optional")
    why = r.get("why")
    if not isinstance(why, str) or len(why.strip()) < 20:
        warn(where, "resource.why missing or under 20 chars — say why this one")
    elif len(why) > 500:
        err(where, "resource.why over 500 chars")
    y = r.get("year")
    if y is not None and not (isinstance(y, int) and 1600 <= y <= 2100):
        err(where, f"resource.year {y!r} is not a plausible year")
    v = r.get("verified")
    if v is not None and not (isinstance(v, str) and re.fullmatch(r"\d{4}-\d{2}-\d{2}", v)):
        err(where, f"resource.verified {v!r} is not YYYY-MM-DD")


def check_text(where, s, allow_unicode=False, is_code=False):
    if EMOJI.search(s):
        err(where, "contains emoji")
    if not allow_unicode:
        prose = strip_math(strip_code(s))
        bad = sorted({c for c in prose if c in BANNED})
        if bad:
            err(where, f"raw Unicode math outside $...$: {''.join(bad)} — use LaTeX")
    # Unbalanced math delimiters. CONTENT-SPEC 128 exempts "an L0.body that is
    # source code", and concept.php renders L0.body with Markup::code() -- never
    # as markdown, never through KaTeX -- so a `$` there is a shell prompt, a
    # Make variable or a PHP sigil, not an unclosed math span. Running the check
    # anyway produced false errors that 37 concepts worked around by wrapping
    # L0.body in a ``` fence, which then rendered as literal backticks.
    if is_code:
        return
    body = strip_code(s)
    if body.count("$$") % 2:
        err(where, "unbalanced $$ display-math delimiters")
    singles = len(re.findall(r"(?<!\$)\$(?!\$)", body.replace("$$", "")))
    if singles % 2:
        err(where, "unbalanced $ inline-math delimiters")



# ---------------------------------------------------------------------------
# answer_expr: the machine-checkable half of a numeric answer.
#
# `answer` is prose written for the reveal panel ("For n=1000: 1023 copies")
# and no grader can parse it. `answer_expr` is the same answer written as
# arithmetic over the template's own params, and it is the only thing the drill
# loop can check the learner against. A numeric template without one is
# silently downgraded to self-assessment at review time.
#
# This is a deliberate re-implementation of app/src/Drill/Expr.php: same
# operators, same function whitelist, same refusals. It exists so the authoring
# gate rejects an expression the application would fail on, and so a mismatch
# between the two shows up here rather than in front of a learner.

EXPR_FUNCS = {"sqrt": 1, "abs": 1, "floor": 1, "ceil": 1, "round": 1, "ln": 1, "log": 1,
              "log2": 1, "log10": 1, "exp": 1, "min": 2, "max": 2, "pow": 2, "mod": 2}
EXPR_CONSTS = {"pi": math.pi, "e": math.e}
EXPR_OPS = {"+": (2, False), "-": (2, False), "*": (3, False), "/": (3, False),
            "%": (3, False), "u-": (4, True), "^": (5, True)}


def expr_tokens(s):
    out, i, n, prev = [], 0, len(s), None
    while i < n:
        c = s[i]
        if c.isspace():
            i += 1
            continue
        if c.isdigit() or (c == "." and i + 1 < n and s[i + 1].isdigit()):
            j = i
            while j < n and (s[j].isdigit() or s[j] in "._"):
                j += 1
            if j < n and s[j] in "eE" and j + 1 < n and (
                    s[j + 1].isdigit() or (s[j + 1] in "+-" and j + 2 < n and s[j + 2].isdigit())):
                j += 2
                while j < n and s[j].isdigit():
                    j += 1
            prev = ("num", s[i:j].replace("_", ""))
            out.append(prev); i = j; continue
        if c.isalpha() or c == "_":
            j = i
            while j < n and (s[j].isalnum() or s[j] == "_"):
                j += 1
            word, k = s[i:j], j
            while k < n and s[k].isspace():
                k += 1
            isf = k < n and s[k] == "(" and word.lower() in EXPR_FUNCS
            prev = ("func", word.lower()) if isf else ("name", word)
            out.append(prev); i = j; continue
        if c in "(),":
            prev = ("comma" if c == "," else ("lp" if c == "(" else "rp"), c)
            out.append(prev); i += 1; continue
        if c == "*" and i + 1 < n and s[i + 1] == "*":
            prev = ("op", "^"); out.append(prev); i += 2; continue
        if c in EXPR_OPS:
            unary = c == "-" and (prev is None or prev[0] in ("op", "lp", "comma"))
            prev = ("op", "u-" if unary else c)
            out.append(prev); i += 1; continue
        raise ValueError("unexpected character %r" % c)
    return out


def expr_rpn(tokens):
    out, st = [], []
    for t in tokens:
        ty, val = t
        if ty in ("num", "name"):
            out.append(t)
        elif ty == "func":
            st.append(t)
        elif ty == "comma":
            while st and st[-1][0] != "lp":
                out.append(st.pop())
            if not st:
                raise ValueError("misplaced comma")
        elif ty == "op":
            p, right = EXPR_OPS[val]
            while val != "u-" and st and st[-1][0] == "op":
                tp = EXPR_OPS[st[-1][1]][0]
                if tp > p or (not right and tp == p):
                    out.append(st.pop())
                else:
                    break
            st.append(t)
        elif ty == "lp":
            st.append(t)
        elif ty == "rp":
            while st and st[-1][0] != "lp":
                out.append(st.pop())
            if not st:
                raise ValueError("unbalanced parentheses")
            st.pop()
            if st and st[-1][0] == "func":
                out.append(st.pop())
    while st:
        t = st.pop()
        if t[0] == "lp":
            raise ValueError("unbalanced parentheses")
        out.append(t)
    return out


def expr_call(f, a):
    if f == "sqrt":
        if a[0] < 0: raise ValueError("sqrt of negative")
        return math.sqrt(a[0])
    if f == "abs": return abs(a[0])
    if f == "floor": return math.floor(a[0])
    if f == "ceil": return math.ceil(a[0])
    if f == "round": return math.floor(a[0] + 0.5) if a[0] >= 0 else math.ceil(a[0] - 0.5)
    if f in ("ln", "log"):
        if a[0] <= 0: raise ValueError("log of a non-positive number")
        return math.log(a[0])
    if f == "log2":
        if a[0] <= 0: raise ValueError("log2 of a non-positive number")
        return math.log(a[0], 2)
    if f == "log10":
        if a[0] <= 0: raise ValueError("log10 of a non-positive number")
        return math.log10(a[0])
    if f == "exp": return math.exp(a[0])
    if f == "min": return min(a[0], a[1])
    if f == "max": return max(a[0], a[1])
    if f == "pow": return a[0] ** a[1]
    if f == "mod":
        if a[1] == 0: raise ValueError("division by zero")
        return math.fmod(a[0], a[1])
    raise ValueError("unknown function %s" % f)


def expr_eval(expr, vars):
    """Evaluate expr over vars, or raise ValueError. No eval(), no builtins."""
    if len(expr) > 400:
        raise ValueError("expression longer than 400 characters")
    st = []
    for ty, val in expr_rpn(expr_tokens(expr)):
        if ty == "num":
            st.append(float(val))
        elif ty == "name":
            low = val.lower()
            if val in vars: st.append(float(vars[val]))
            elif low in vars: st.append(float(vars[low]))
            elif low in EXPR_CONSTS: st.append(EXPR_CONSTS[low])
            else: raise ValueError("unknown variable %r" % val)
        elif ty == "op":
            if val == "u-":
                if not st: raise ValueError("bad expression")
                st.append(-st.pop()); continue
            if len(st) < 2: raise ValueError("bad expression")
            b, a = st.pop(), st.pop()
            if val == "+": st.append(a + b)
            elif val == "-": st.append(a - b)
            elif val == "*": st.append(a * b)
            elif val in "/%":
                if b == 0: raise ValueError("division by zero")
                st.append(a / b if val == "/" else math.fmod(a, b))
            elif val == "^":
                r = a ** b
                if isinstance(r, complex): raise ValueError("complex result")
                st.append(float(r))
        elif ty == "func":
            ar = EXPR_FUNCS[val]
            if len(st) < ar: raise ValueError("bad call to %s()" % val)
            args = [st.pop() for _ in range(ar)][::-1]
            st.append(expr_call(val, args))
    if len(st) != 1:
        raise ValueError("bad expression")
    if not math.isfinite(st[0]):
        raise ValueError("does not evaluate to a finite number")
    return st[0]


def expr_names(expr):
    return {v for ty, v in expr_tokens(expr) if ty == "name"}


def check_answer_expr(qw, q, params):
    """CONTENT-SPEC §4: a numeric grader ships an expression and a tolerance."""
    grader = q.get("grader")
    expr = q.get("answer_expr")
    if expr is not None and not isinstance(expr, str):
        err(qw, "answer_expr must be a string")
        return
    if grader != "numeric":
        if isinstance(expr, str) and expr.strip():
            warn(qw, "answer_expr is only evaluated by the numeric grader")
        if q.get("tolerance") is not None:
            warn(qw, f"tolerance is dead on a {grader!r} grader")
        return

    tol = q.get("tolerance")
    if tol is None or isinstance(tol, bool) or not isinstance(tol, (int, float)):
        err(qw, "numeric grader needs an explicit tolerance (relative; 0.02 is 2%)")
    elif not (0 <= tol < 1):
        err(qw, f"tolerance {tol} is not a relative fraction in [0, 1)")

    if not isinstance(expr, str) or not expr.strip():
        err(qw, "numeric grader needs an answer_expr — the arithmetic form of the "
                "answer, over this template's own params. Without it the drill loop "
                "cannot grade the item and silently downgrades it to self-assessment.")
        return
    expr = expr.strip()

    try:
        names = expr_names(expr)
    except ValueError as e:
        err(qw, f"answer_expr does not parse: {e}")
        return
    undeclared = sorted(n for n in names if n not in params and n.lower() not in EXPR_CONSTS)
    if undeclared:
        err(qw, f"answer_expr names {undeclared} which are not in params")
        return
    nonnumeric = sorted(
        n for n in names if n in params
        and not all(is_number(v) for v in (params[n] if isinstance(params[n], list) else [params[n]]))
    )
    if nonnumeric:
        err(qw, f"answer_expr uses {nonnumeric}, whose draws are not all numeric — "
                "the evaluator only ever sees numeric slots")
        return

    # Every draw, capped, because an expression that works on the first
    # combination and divides by zero on the fourth is a review-time failure.
    keys = list(params)
    lists = [params[k] if isinstance(params[k], list) else [params[k]] for k in keys]
    n = 0
    for tup in itertools.product(*lists) if keys else [()]:
        if n >= 200:
            break
        n += 1
        env = {k: float(v) for k, v in zip(keys, tup) if is_number(v)}
        try:
            expr_eval(expr, env)
        except ValueError as e:
            draw = ", ".join(f"{k}={v}" for k, v in zip(keys, tup))
            err(qw, f"answer_expr fails at {draw or 'no params'}: {e}")
            return


def is_number(v):
    if isinstance(v, bool):
        return False
    if isinstance(v, (int, float)):
        return True
    if isinstance(v, str):
        try:
            float(v)
            return True
        except ValueError:
            return False
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--source", default=os.path.join(ROOT, "depthmap.json"))
    ap.add_argument("--todo", action="store_true", help="also print the v2 upgrade to-do lines (bare-URL resources etc.)")
    a = ap.parse_args()

    with open(a.path) as f:
        try:
            doc = json.load(f)
        except json.JSONDecodeError as e:
            print(f"ERROR  file: invalid JSON — {e}")
            return 1

    # ---- domain header
    d = doc.get("domain")
    if not isinstance(d, dict):
        err("domain", "missing")
        print("\n".join(errors))
        return 1
    for k in ("id", "n", "title", "color", "tag", "why"):
        if not d.get(k):
            err("domain", f"missing '{k}'")
    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", d.get("color", "")):
        err("domain", f"color must be #RRGGBB, got {d.get('color')!r}")

    # ---- people
    people = doc.get("people", [])
    names = set()
    if not isinstance(people, list) or not (6 <= len(people) <= 20):
        err("people", f"expected 6-20 entries, got {len(people) if isinstance(people, list) else 'none'}")
    for i, p in enumerate(people if isinstance(people, list) else []):
        w = f"people[{i}]"
        for k in ("name", "role", "contribution"):
            if not p.get(k):
                err(w, f"missing '{k}'")
        names.add(p.get("name"))
        x = p.get("x")
        if x is not None:
            if not re.fullmatch(r"https://(x|twitter)\.com/[A-Za-z0-9_]{1,15}/?", x):
                err(w, f"malformed X url: {x!r}")
            if p.get("verified") is not True:
                warn(w, "X url present but verified is not true")
        if len(p.get("contribution", "")) < 40:
            warn(w, "contribution is thin — name the paper, system or tool")

    check_uid("domain", d)

    # ---- sections and concepts
    titles, all_prereqs, graph = [], set(), {}
    n_concepts = n_preserved = n_q = 0

    secs = doc.get("sections")
    if not isinstance(secs, list) or not secs:
        err("sections", "missing or empty")
        secs = []

    for si, sec in enumerate(secs):
        sw = f"sections[{si}]"
        check_uid(sw, sec)
        if not sec.get("t"):
            err(sw, "missing title")
        cs = sec.get("concepts")
        if not isinstance(cs, list) or not cs:
            err(sw, "no concepts")
            continue
        for ci, c in enumerate(cs):
            t = c.get("t", f"<untitled {si}.{ci}>")
            w = f"{d.get('n')}·{sec.get('t','?')[:24]}·{t[:40]}"
            check_uid(w, c)
            n_concepts += 1
            if c.get("preserved"):
                n_preserved += 1
            if t in titles:
                err(w, "duplicate concept title in this domain")
            titles.append(t)

            # L0
            l0 = c.get("L0")
            if not isinstance(l0, dict) or not l0.get("body") or not l0.get("cloze"):
                err(w, "L0 must be an object with 'body' and 'cloze'")
            else:
                if "{{c" not in l0["cloze"]:
                    err(w, "L0.cloze has no {{c1::...}} marker")
                if not (40 <= len(l0["body"]) <= 600):
                    warn(w, f"L0.body length {len(l0['body'])} outside 40-600")
                # L0.body is rendered with Markup::code(), so a markdown fence
                # is not stripped -- it reaches the learner as literal backticks.
                if "```" in l0["body"]:
                    err(w + " L0.body", "contains a ``` fence; L0.body is already "
                                        "rendered as code, so the fence renders literally")
                check_text(w + " L0.body", l0["body"], allow_unicode=True, is_code=True)

            # L1/L2/L3
            for layer, (lo, hi) in LEN.items():
                v = c.get(layer)
                if not isinstance(v, str) or not v.strip():
                    err(w, f"{layer} missing")
                    continue
                n = len(v)
                if not (lo <= n <= hi):
                    # preserved L1/L2 come from source and are exempt
                    if c.get("preserved") and layer in ("L1", "L2"):
                        pass
                    else:
                        warn(w, f"{layer} length {n} outside {lo}-{hi}")
                # preserved L1/L2 are copied byte-for-byte from depthmap.json and
                # may legitimately contain raw Unicode the author cannot alter.
                exempt = bool(c.get("preserved")) and layer in ("L1", "L2")
                check_text(f"{w} {layer}", v, allow_unicode=exempt)

            # L4
            qs = c.get("L4")
            # v2 (PLAN-V2 §1.4) targets >=3 tier-1, >=2 tier-2, >=2 tier-3 per
            # concept; the ceiling is generous, the floor is still 1 until the
            # deepening pass lands. Tier coverage is reported, not enforced, by
            # build/validate_corpus.py.
            if not isinstance(qs, list) or not (1 <= len(qs) <= 12):
                err(w, "L4 must be a list of 1-12 templates")
                qs = []
            for qi, q in enumerate(qs):
                n_q += 1
                qw = f"{w} L4[{qi}]"
                check_uid(qw, q)
                tier = q.get("tier", 1)
                if tier not in (1, 2, 3):
                    err(qw, f"tier must be 1, 2 or 3 (got {tier!r})")
                if q.get("kind") not in KINDS:
                    err(qw, f"bad kind {q.get('kind')!r}")
                if q.get("grader") not in GRADERS:
                    err(qw, f"bad grader {q.get('grader')!r}")
                tpl = q.get("prompt_tpl", "")
                if not tpl:
                    err(qw, "missing prompt_tpl")
                params = q.get("params", {})
                if not isinstance(params, dict):
                    err(qw, "params must be an object")
                    params = {}
                slots = set(re.findall(r"\{([A-Za-z_][A-Za-z0-9_]*)\}", tpl))
                missing = slots - set(params)
                if missing:
                    err(qw, f"prompt slots with no params: {sorted(missing)}")
                unused = set(params) - slots
                if unused:
                    warn(qw, f"params never used in prompt: {sorted(unused)}")
                for k, v in params.items():
                    if not isinstance(v, list) or not v:
                        err(qw, f"params[{k}] must be a non-empty list")
                if q.get("grader") == "mcq":
                    o = q.get("options")
                    if not isinstance(o, list) or len(o) != 3:
                        err(qw, f"mcq needs exactly 3 options, got {len(o) if isinstance(o,list) else 'none'}")
                if q.get("answer") in (None, ""):
                    err(qw, "missing answer")
                check_answer_expr(qw, q, params)
                exp = q.get("explanation", "")
                if not (100 <= len(exp) <= 600):
                    warn(qw, f"explanation length {len(exp)} outside 100-600")
                check_text(qw, tpl + " " + str(q.get("answer", "")) + " " + exp)

            # mcq-only check
            if qs and all(q.get("grader") == "mcq" for q in qs):
                err(w, "every L4 is mcq — recognition is weak; add a recall item")

            # people refs
            for pn in c.get("people", []) or []:
                if pn not in names:
                    warn(w, f"people ref {pn!r} not in domain people list")

            graph[t] = list(c.get("prereqs", []) or [])
            all_prereqs.update(graph[t])

            r = c.get("resources", []) or []
            if len(r) > 8:
                warn(w, f"{len(r)} resources — cap at 8")
            for ri, u in enumerate(r):
                check_resource(f"{w} resources[{ri}]", u)

    # ---- prereq DAG (within-domain edges only; cross-domain refs are allowed dangling)
    known = set(titles)
    local_quals = {d.get("id"), d.get("n")}
    internal, external = {}, set()
    for k, v in graph.items():
        here = []
        for p in v:
            qual, title = split_prereq(p)
            if qual is not None and qual not in local_quals:
                external.add(p)          # qualified at another domain
                continue
            if qual is not None and title not in known:
                err("prereqs", f"{k!r}: prereq {p!r} is qualified at this domain "
                               f"but {title!r} is not a concept here")
                continue
            if title in known:
                here.append(title)
            else:
                external.add(p)
        internal[k] = here
    color = {}

    def dfs(u, stack):
        color[u] = 1
        for v in internal.get(u, []):
            if color.get(v) == 1:
                cyc = stack[stack.index(v):] + [v] if v in stack else [u, v]
                err("prereqs", "cycle: " + " -> ".join(cyc))
                return
            if color.get(v, 0) == 0:
                dfs(v, stack + [v])
        color[u] = 2

    for t in internal:
        if color.get(t, 0) == 0:
            dfs(t, [t])

    dangling = sorted(external)
    if dangling:
        warn("prereqs", f"{len(dangling)} cross-domain refs (ok if intentional): {dangling[:8]}")

    # ---- preserved integrity against source
    if os.path.exists(a.source):
        src = json.load(open(a.source))
        sd = next((x for x in src if x["id"] == d.get("id")), None)
        if sd:
            want = {}
            for s in sd["sections"]:
                for it in s["items"]:
                    want[it["t"]] = (it["d"], it.get("m") or "")
            have = {}
            for s in secs:
                for c in s.get("concepts", []):
                    if c.get("preserved"):
                        have[c.get("t")] = (c.get("L1"), c.get("L2"))
            for t, (dd, mm) in want.items():
                if t not in have:
                    err("preserved", f"source topic missing from output: {t!r}")
                else:
                    if have[t][0] != dd:
                        err("preserved", f"L1 differs from source 'd' for {t!r}")
                    if have[t][1] != mm:
                        err("preserved", f"L2 differs from source 'm' for {t!r}")
            extra = set(have) - set(want)
            if extra:
                err("preserved", f"marked preserved but not in source: {sorted(extra)[:5]}")

    # ---- report
    if a.todo:
        for line in todo:
            print(line)
    for line in warnings:
        print(line)
    for line in errors:
        print(line)
    print(f"\n{os.path.basename(a.path)}: {n_concepts} concepts "
          f"({n_preserved} preserved), {n_q} questions, {len(people)} people, "
          f"{len(errors)} errors, {len(warnings)} warnings, {len(todo)} v2-todo")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
