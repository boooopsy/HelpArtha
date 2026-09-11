# Borrow Checker Matrix (P16_1)

**Module:** Rust Systems Programming, Affine Types & Memory Safety (`module16_rust_safety`)  
**Classification:** Alpha (Tactile)  

## 1. Project Objective
Resolve 20 intentionally broken Rust programs without resorting to .clone() or reference counting.

## 2. Mental Model & Physical Analogy
Every resource has a single owner. Ownership can be moved or temporarily lent out, but data cannot be mutated while shared references exist.

## 3. Bill of Materials / Tools
Rust toolchain (rustc, cargo, clippy, miri).
