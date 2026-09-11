# Lock-Free SPSC Ring Buffer (P15_3)

**Module:** Concurrency, Atomics & Memory Consistency Models (`module15_concurrency_atomics`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Build a single-producer single-consumer queue utilizing explicit acquire-release memory fences.

## 2. Mental Model & Physical Analogy
Without coordination, multiple CPU cores accessing shared memory will overwrite each other's data. Memory consistency models define the rules for when writes by one core become visible to others.

## 3. Bill of Materials / Tools
Multi-core development workstation, ThreadSanitizer (TSan).
