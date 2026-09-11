# Module 16: Rust Systems Programming, Affine Types & Memory Safety

**Tier:** `tier1_core_systems`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Every resource has a single owner. Ownership can be moved or temporarily lent out, but data cannot be mutated while shared references exist.

## 2. Core Primitives
Affine type systems, linear logic, ownership, move semantics, copy semantics, Drop trait, RAII; the borrow checker: (Shared AND NOT Mutable) OR (NOT Shared AND Mutable); lexical vs non-lexical lifetimes, annotations ('a); safe vs unsafe Rust, raw pointers, thread marker traits (Send and Sync).

## 3. Physical & Virtual Workbenches (BOM)
Rust toolchain (rustc, cargo, clippy, miri).

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Steve Klabnik & Carol Nichols - The Rust Programming Language (The Official Book)](https://doc.rust-lang.org/book/)
- **[Textbook]** [Jon Gjengset - Rust for Rustaceans: Idiomatic Programming for Experienced Developers](https://nostarch.com/rust-rustaceans)
- **[Textbook]** [Mara Bos - Rust Atomics and Locks: Low-Level Concurrency in Practice (O'Reilly)](https://marabos.nl/atomics/)
- **[Seminal Paper]** [Nicholas D. Matsakis & Felix S. Klock II - The Rust Language: Affine Types & Borrow Checking](https://dl.acm.org/doi/10.1145/2663171.2663188)

## 5. Standardized Milestone Projects
- **P16_1 (Alpha (Tactile))**: Borrow Checker Matrix — Resolve 20 intentionally broken Rust programs without resorting to .clone() or reference counting.
- **P16_2 (Beta (Milestone))**: Memory-Safe Doubly-Linked List — Implement a doubly-linked list comparing safe abstraction patterns against raw unsafe pointers.
- **P16_3 (Gamma (Capstone))**: Multi-Threaded Worker Pool — Build a thread pool in Rust that dispatches jobs over crossbeam channels with panic recovery.
