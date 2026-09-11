# 64-Byte Cache-Conscious B-Tree (P23_2)

**Module:** Cache-Conscious Data Structures, B-Trees & Locality (`module23_cache_locality`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Implement a B-Tree in C/Rust with node sizing matched to 64-byte cache lines; benchmark vs binary trees.

## 2. Mental Model & Physical Analogy
Pointer chasing across RAM introduces significant memory latency. Cache-conscious data structures group contiguous data together into blocks sized to match CPU cache lines.

## 3. Bill of Materials / Tools
Hardware performance counter profiler (perf on Linux).
