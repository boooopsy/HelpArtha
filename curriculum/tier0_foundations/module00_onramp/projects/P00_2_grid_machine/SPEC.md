# Specification & Invariant Contracts: P00_2 Token Grid State Machine

## 1. Input/Output Contract
- **Input**: `{"cells": [int, ...]}`, 1-8 integers.
- **Output**: `{"cells", "sorted_cells", "comparisons", "swaps", "trace"}`.
- **Core invariant**: `sorted_cells` is always a permutation of `cells`
  in non-decreasing order — no token is created, destroyed, or
  duplicated, only moved (conservation of tokens on the grid).

## 2. Prohibited Libraries & Magic
- Strictly prohibited: `random`, `time`, `eval`, `exec`, `subprocess`,
  `urllib`, `requests`, and any built-in `sort`/`sorted` call — the
  point of this project is to perform the comparisons and swaps
  yourself, like the pointer physically walking the grid.

## 3. Test Coverage Matrix
8 deterministic vectors covering: an already-sorted row (zero swaps),
a fully reversed row (maximum swaps), a row with duplicate values, a
single-cell row (trivial case), a two-cell row, a row needing exactly
one swap, a full 8-cell row, and a cross-check that comparisons always
equals swaps + non-swaps for the recorded trace.
