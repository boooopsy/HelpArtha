# Cache-Stride Latency Benchmark (P08_3)

**Module:** Systems C Programming, Memory Topology & Pointers (`module08_systems_c`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Build a diagnostic harness in C measuring latency cliffs as stride lengths exceed 64-byte lines.

## 2. Mental Model & Physical Analogy
Memory is a single-dimensional array of 8-bit cubbies. A pointer is an index into that array. Dereferencing is opening the cubby at that index to read or write its contents.

## 3. Bill of Materials / Tools
Memory layout diagram chart, hardware address decoder simulator.
