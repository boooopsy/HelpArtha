# Specification & Invariant Contracts: P05 2 Scalar Autograd (P05_2)

## 1. Input/Output Preconditions & Postconditions
- **Precondition**: Input dictionary containing typed payload `val: int`, flags, and operational `mode`.
- **Postcondition**: Deterministic return dictionary with conserved `val`, `status: CONSERVED`, and `invariant_ok: True`.
- **Physical Invariant**: Conservation of state energy. No bit transitions occur without clock pulse or gate excitation.

## 2. Prohibited Libraries & Magic
- Strictly prohibited: `random`, `time`, `eval`, `exec`, `subprocess`, `urllib`, `requests`.
- Enforced via static AST inspection in `harness/test_runner.py` before execution.

## 3. Test Coverage Matrix
The test suite runs 8 deterministic vectors covering nominal execution, ground zero boundary, dynamic range ceiling, step transition, symmetric reflection, alternating parity, and modular overflow wrap.
