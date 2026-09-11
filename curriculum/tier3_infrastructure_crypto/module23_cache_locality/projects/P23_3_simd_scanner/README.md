# SIMD-Accelerated Vector Scanner (P23_3)

**Module:** Cache-Conscious Data Structures, B-Trees & Locality (`module23_cache_locality`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Write a search engine in C using AVX2/NEON intrinsics scanning 8 keys per clock cycle without branching.

## 2. Mental Model & Physical Analogy
Pointer chasing across RAM introduces significant memory latency. Cache-conscious data structures group contiguous data together into blocks sized to match CPU cache lines.

## 3. Bill of Materials / Tools
Hardware performance counter profiler (perf on Linux).
