# Module 15: Concurrency, Atomics & Memory Consistency Models

**Tier:** `tier1_core_systems`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Without coordination, multiple CPU cores accessing shared memory will overwrite each other's data. Memory consistency models define the rules for when writes by one core become visible to others.

## 2. Core Primitives
Critical sections, race conditions, mutual exclusion, deadlocks, livelocks, priority inversion; atomic instructions: TAS, CAS, FAA; memory consistency models: Sequential consistency, relaxed consistency, acquire-release semantics, memory barriers/fences, compiler and hardware out-of-order reordering.

## 3. Physical & Virtual Workbenches (BOM)
Multi-core development workstation, ThreadSanitizer (TSan).

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Maurice Herlihy & Nir Shavit - The Art of Multiprocessor Programming (Revised 1st Edition)](https://www.elsevier.com/books/the-art-of-multiprocessor-programming/herlihy/978-0-12-370591-4)
- **[Textbook]** [Paul E. McKenney - Is Parallel Programming Hard, And, If So, What Can You Do About It? (Perfbook)](https://kernel.org/pub/linux/kernel/people/paulmck/perfbook/perfbook.html)
- **[Seminal Paper]** [Hans-J. Boehm - Threads Cannot be Implemented as a Library (PLDI 2005)](https://dl.acm.org/doi/10.1145/1065010.1065042)
- **[Seminal Paper]** [Sarita V. Adve & Kourosh Gharachorloo - Shared Memory Consistency Models: A Tutorial (1996)](https://ieeexplore.ieee.org/document/546611)

## 5. Standardized Milestone Projects
- **P15_1 (Alpha (Tactile))**: Race Condition Stress Lab — Multi-threaded program demonstrating data corruption on shared balances without synchronization.
- **P15_2 (Beta (Milestone))**: Ticket Lock & Spinlock in C — Implement fair mutual-exclusion locks using GCC atomic built-ins (__atomic_compare_exchange_n).
- **P15_3 (Gamma (Capstone))**: Lock-Free SPSC Ring Buffer — Build a single-producer single-consumer queue utilizing explicit acquire-release memory fences.
