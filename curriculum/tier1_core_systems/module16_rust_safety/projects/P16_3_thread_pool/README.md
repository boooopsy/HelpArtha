# Multi-Threaded Worker Pool (P16_3)

**Module:** Rust Systems Programming, Affine Types & Memory Safety (`module16_rust_safety`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Build a thread pool in Rust that dispatches jobs over crossbeam channels with panic recovery.

## 2. Mental Model & Physical Analogy
Every resource has a single owner. Ownership can be moved or temporarily lent out, but data cannot be mutated while shared references exist.

## 3. Bill of Materials / Tools
Rust toolchain (rustc, cargo, clippy, miri).
