# Byte-Aligned Slab/Arena Allocator (P08_2)

**Module:** Systems C Programming, Memory Topology & Pointers (`module08_systems_c`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Write a custom arena allocator in C featuring out-of-memory guards and reset capabilities.

## 2. Mental Model & Physical Analogy
Memory is a single-dimensional array of 8-bit cubbies. A pointer is an index into that array. Dereferencing is opening the cubby at that index to read or write its contents.

## 3. Bill of Materials / Tools
Memory layout diagram chart, hardware address decoder simulator.
