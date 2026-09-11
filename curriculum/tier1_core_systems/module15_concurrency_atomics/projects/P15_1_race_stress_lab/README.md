# Race Condition Stress Lab (P15_1)

**Module:** Concurrency, Atomics & Memory Consistency Models (`module15_concurrency_atomics`)  
**Classification:** Alpha (Tactile)  

## 1. Project Objective
Multi-threaded program demonstrating data corruption on shared balances without synchronization.

## 2. Mental Model & Physical Analogy
Without coordination, multiple CPU cores accessing shared memory will overwrite each other's data. Memory consistency models define the rules for when writes by one core become visible to others.

## 3. Bill of Materials / Tools
Multi-core development workstation, ThreadSanitizer (TSan).
