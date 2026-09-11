# Memory-Safe Doubly-Linked List (P16_2)

**Module:** Rust Systems Programming, Affine Types & Memory Safety (`module16_rust_safety`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Implement a doubly-linked list comparing safe abstraction patterns against raw unsafe pointers.

## 2. Mental Model & Physical Analogy
Every resource has a single owner. Ownership can be moved or temporarily lent out, but data cannot be mutated while shared references exist.

## 3. Bill of Materials / Tools
Rust toolchain (rustc, cargo, clippy, miri).
