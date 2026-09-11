# Specification & Invariant Contracts: P00_1 Marble Counter

## 1. Input/Output Contract
- **Input**: `{"start": int (0-7), "pulses": int (>=0)}`.
- **Output**: `{"start", "pulses", "final_value", "trace", "wraps"}`.
- **Core invariant**: the register only ever holds a value 0-7. Any 4th
  bit "falls off the edge" — this is the wraparound a physical 3-bit
  counter shows as all three gear-bits flipping back to 0 at once.

## 2. Prohibited Libraries & Magic
- Strictly prohibited: `random`, `time`, `eval`, `exec`, `subprocess`,
  `urllib`, `requests`.
- Enforced via static AST inspection in `harness/test_runner.py`.

## 3. Test Coverage Matrix
8 deterministic vectors covering: zero pulses (no-op), a single pulse,
a full loop of exactly 8 pulses (returns to start), an odd starting
value, wraparound mid-sequence, starting already at the maximum value
(7), a long run crossing multiple wraps, and a full 3-bit period
verifying the trace matches manual binary counting exactly.
