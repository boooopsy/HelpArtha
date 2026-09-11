# Ticket Lock & Spinlock in C (P15_2)

**Module:** Concurrency, Atomics & Memory Consistency Models (`module15_concurrency_atomics`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Implement fair mutual-exclusion locks using GCC atomic built-ins (__atomic_compare_exchange_n).

## 2. Mental Model & Physical Analogy
Without coordination, multiple CPU cores accessing shared memory will overwrite each other's data. Memory consistency models define the rules for when writes by one core become visible to others.

## 3. Bill of Materials / Tools
Multi-core development workstation, ThreadSanitizer (TSan).
