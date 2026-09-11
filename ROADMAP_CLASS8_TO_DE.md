# Path: Class 8 Student → Distinguished Engineer

This is the real, practical route through Whetstone for a learner starting
around **class 8 (age ~13)**, with no assumed background. It reuses the
existing 5-tier structure but reframes pacing, checkpoints, and what
"done" looks like at each stage for a young learner rather than an adult
career-changer.

Two ground rules that shape everything below:
1. **A concept doesn't count as learned until it's been drilled and
   retrieved from memory, not just read once.** Reading is the easy
   10%. Spaced repetition (FSRS-6) is the mechanism; heavy repetition
   is fine and expected, but every rep must be a genuinely different
   question, never the same text with a number swapped.
2. **Every tier ends with something built, not just something known.**
   A checkpoint is a working artifact (program, circuit, proof, writeup)
   the learner can point to, not a quiz score.

---

## Stage 1 — Class 8-9 (age ~13-14): Foundations & the Concrete On-Ramp
**Tiers/domains:** `00b` computer ramp, `00a` maths ramp, `module00_onramp`,
early `00` foundations (bits, bytes, variables, loops).
**Pace:** slow, tactile, mostly off-screen at first (Turing Tumble,
physical counting, typing practice) before any real code.
**What "done" looks like:** can explain what a bit/byte/variable is
without hesitating; can type without hunting for keys; can predict what
a 3-bit counter or a comparator does by hand before checking the
computer.
**Checkpoint artifact:** the three module00 tactile projects, done for
real — a working 3-bit counter simulation, a working bubble-sort grid
runner, a working stream comparator (these three now have real code
and real tests — see FIX_LOG.md).

## Stage 2 — Class 9-10 (age ~14-16): Real Programming + Discrete Math
**Tiers/domains:** `00c` mathematics (algebra, basic discrete math),
`01` languages (Python fundamentals), `02` algorithms (basics), `06`
command line.
**Pace:** first real programs — not toy exercises, small useful tools
(a to-do list, a simple grade calculator, a text adventure). First
encounter with Big-O as "why does my program get slow."
**Checkpoint artifact:** 3-5 small original Python programs the
learner designed themselves (not copied from a tutorial), each with
basic tests.

## Stage 3 — Class 11-12 (age ~16-18): Systems Fundamentals
**Tiers/domains:** `04` architecture, `05` operating systems, `08`
databases (basics), `17` digital design (intro), start of `linear
algebra`/`calculus` proper.
**Pace:** this is where "how does the machine actually work" opens up
— memory, the OS, how a database stores things, first digital logic
(gates, flip-flops). This maps to what a strong CS-focused high-schooler
studies before university, done properly instead of superficially.
**Checkpoint artifact:** a from-scratch small project touching real
systems concepts — e.g. a simple key-value store, a tiny OS scheduler
simulation, or a breadboard digital-logic circuit that actually works.

## Stage 4 — Undergrad years (age ~18-22): Core CS Degree, Done for Real
**Tiers/domains:** full `01`-`09`, `17`-`19` (languages, algorithms,
architecture, OS, command line, distributed systems intro, databases,
caching, digital design, chip architecture intro, networking).
**Pace:** this is the traditional 4-year CS degree core, but drilled to
retention instead of crammed for an exam and forgotten. Real internship-
grade projects, first open-source contributions.
**Checkpoint artifact:** 1-2 substantial projects with real users or
real published code (a working web service, a contribution merged
into a real open-source project, a small compiler or interpreter).

## Stage 5 — Early career (age ~22-26): Systems Depth + Specialization Begins
**Tiers/domains:** `07` distributed systems, `10` data engineering,
`11` system design, `12` ML foundations, `15` numerics, `20` security.
**Pace:** production engineering — the stuff that only shows up once
you're responsible for something real running in the world. This is
also where the learner picks a lane: infra/distributed systems,
hardware/silicon, or ML/AI systems.
**Checkpoint artifact:** a system design writeup defended against real
critique, plus production experience on a real (even small) service.

## Stage 6 — Mid-career (age ~26-33): Deep Specialization
**Tiers/domains:** depending on the chosen lane — `13` LLMs, `16` GPU
kernels, `18` chip architecture, `21` research practice; or continued
depth in `07`/`11` for the infra lane.
**Pace:** this is genuinely hard, narrow, high-value work. Public
artifacts matter enormously here (published writeups, open-source
kernels, reproduced papers) — `21` research-practice exists specifically
to build that habit.
**Checkpoint artifact:** a public technical artifact good enough to be
a credential on its own — a benchmarked kernel, a published
reproduction of a real paper, a meaningful open-source subsystem.

## Stage 7 — Distinguished Engineer (age ~33+)
**Domain:** `14` "the level itself."
**This one is honest, not a knowledge tier.** Distinguished/Fellow status
is a recognition of multi-year, company-scale impact — not a course you
finish. What the earlier stages buy you is the technical range and the
public track record that make that kind of impact possible when the
opportunity shows up.

---

## How the "heavily drilled, but real" part actually works

- Every concept gets multiple genuinely distinct review questions over
  time (recall, applied/computed, misconception-check, deeper
  reasoning) — not the same sentence with a number changed. The
  `content/*.json` L0-L4 layers and FSRS-6 scheduler already do this
  correctly; `module00`'s drill files have now been rewritten to the
  same real standard (see FIX_LOG.md) as the reference pattern for the
  other 28 modules.
- Volume is good and intended — a concept should come back for review
  many times over weeks/months. The fix is never "drill less," it's
  "make every rep a real, different question."
- Projects are the other half of retention: a project's tests must
  verify the SPECIFIC behavior of that specific mechanism (a counter's
  wraparound, a sort's comparison count, a comparator's halt point),
  never a generic "value came back unchanged" check that would pass
  for literally any project.
