# Fix Log — Content Quality Pass

## Status: Pilot complete on Module 00. 28 modules + full content rewrite remaining.

### What was actually broken (verified by reading every file, not the README)
1. **All 87 `curriculum/*/projects/*/starter/solution.py` files were
   logically identical** — a no-op that echoes `val` back with
   `status: CONSERVED`, regardless of whether the project claimed to be
   a marble counter or a FlashAttention kernel. Verified by diffing the
   normalized body of every file: 1 unique implementation across 87
   files.
2. **All `curriculum/*/drills/L1_mechanics.json` /
   `L2_execution.json` / `L3_invariants.json` files (3,480 questions
   total) were a single Mad-Libs template** — "[Domain - Sprint N]
   Mechanics Check #N: Which core invariant governs state transition
   at step N?" with the same 3 canned options every time, only N
   substituted. This is the flagship, most-promoted UI surface (every
   module card in the "Curriculum" tab has direct "Start L1/L2/L3
   Battery" buttons wired straight to this data).
3. **`content/*.json`'s 24 `domain.why` fields** (shown directly to the
   learner on every domain overview page) were written for an adult
   career-changer audience — interview-signal framing, "L6+", "staff-
   level," India job-market stats — not appropriate for a class 8
   starting point.
4. `content/*.json`'s actual concept bodies (L0-L4, 1,638 concepts) and
   `content/projects.json` (26 weekly + 177 daily projects) were
   already genuinely well-written and did NOT need the same kind of
   fix — they're the reusable good pattern the rest of the repo should
   be brought up to.

### What was fixed in this pass (Module 00 pilot — the reference standard)
- **3/3 projects rewritten with real logic + real tests, verified by
  actually running `harness/test_runner.py`, 8/8 vectors passing on
  each:**
  - `P00_1_marble_counter` — real 3-bit binary counter with wraparound,
    trace, and wrap-count.
  - `P00_2_grid_machine` — real bubble sort with per-step
    comparison/swap trace (token conservation verified).
  - `P00_3_marble_comparator` — real neighbor-mismatch detector with
    correct first-halt-only semantics.
- **42 real, distinct drill questions written for Module 00** (10 L1,
  24 L2 parameterized-and-computed, 8 L3), replacing the templated
  originals. Verified: zero duplicate prompts, every "answer" field
  actually present in its own options list, L2 numeric answers
  computed from the real logic (not hand-typed).
- **All 24 `domain.why` fields rewritten** for a class-8 starting
  reader — plain language, honest about the eventual destination,
  no adult career-market jargon.
- `whetstone-data.js` rebuilt via `build/bundle_data.py`; confirmed the
  new question IDs and rewritten `why` text are present in the output
  bundle.

### What is NOT yet fixed (explicitly, so nothing is assumed done)
- **84 of 87 curriculum projects** still have the no-op stub — every
  tier from digital logic through GPU kernels.
- **28 of 29 modules' drill batteries** (~3,440 questions) still have
  the templated Mad-Libs text.
- **`content/*.json` concept bodies (L0-L4 prose for all 1,638
  concepts)** have not been rewritten for class-8 reading level — only
  the 24 top-level `why` intros were. The concept-level prose is
  currently written at the same adult/technical density seen in the
  `content/00-foundations.json` "bit, byte, word" example from the
  original review.
- **Resource-link precision** (many of the 1,240 external URLs point
  to a course's general index rather than the specific page) has not
  been audited yet — needs an automated link-checker plus manual
  deep-linking, not covered in this pass.

### The standard to hold every future module to (copy this pattern)
1. A project's `solve()` must implement the SPECIFIC mechanism its
   README describes, and `harness/vectors.json` must test that
   specific behavior (edge cases that would actually fail a wrong
   implementation) — verified by running `harness/test_runner.py` and
   getting real PASS output, not just eyeballing the JSON.
2. Drill questions must have unique prompt text across the whole file;
   any parameterized question must compute its "correct" answer from
   the real logic, not hardcode it; run a duplicate-check before
   shipping.
3. Any text a class-8 learner will actually read (`domain.why`,
   concept `L1`, module `spec.md`) must be re-read out loud as "would a
   13-year-old follow this sentence" before it ships.
