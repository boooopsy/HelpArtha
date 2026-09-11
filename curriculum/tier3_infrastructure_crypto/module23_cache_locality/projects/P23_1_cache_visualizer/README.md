# Cache-Line Access Visualizer (P23_1)

**Module:** Cache-Conscious Data Structures, B-Trees & Locality (`module23_cache_locality`)  
**Classification:** Alpha (Tactile)  

## 1. Project Objective
Visual tool mapping memory traversals and displaying cache hits vs. cache misses in real time.

## 2. Mental Model & Physical Analogy
Pointer chasing across RAM introduces significant memory latency. Cache-conscious data structures group contiguous data together into blocks sized to match CPU cache lines.

## 3. Bill of Materials / Tools
Hardware performance counter profiler (perf on Linux).
