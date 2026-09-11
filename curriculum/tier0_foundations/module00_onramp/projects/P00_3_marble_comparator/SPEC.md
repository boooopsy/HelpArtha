# Specification & Invariant Contracts: P00_3 Mechanical Stream Comparator

## 1. Input/Output Contract
- **Input**: `{"stream": [value, ...]}`, 1-8 values (int or str).
- **Output**: `{"stream", "halted", "halt_index", "checks"}`.
- **Core invariant**: the comparator only ever looks at ADJACENT pairs,
  left to right, and stops at the very first mismatch — it never looks
  ahead and never "un-halts" once triggered (matches a physical
  interceptor: once tripped, it stays tripped).

## 2. Prohibited Libraries & Magic
- Strictly prohibited: `random`, `time`, `eval`, `exec`, `subprocess`,
  `urllib`, `requests`.
- Enforced via static AST inspection in `harness/test_runner.py`.

## 3. Test Coverage Matrix
8 deterministic vectors covering: a single-value stream (nothing to
compare, never halts), an all-identical stream, a mismatch at the very
first pair, a mismatch at the very last pair, a mismatch in the middle,
a stream that never halts at all, a stream using strings instead of
numbers, and a mismatch that recurs (verifying it stops at the FIRST
one, not a later one).
