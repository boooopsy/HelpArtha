# Module 23: Cache-Conscious Data Structures, B-Trees & Locality

**Tier:** `tier3_infrastructure_crypto`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Pointer chasing across RAM introduces significant memory latency. Cache-conscious data structures group contiguous data together into blocks sized to match CPU cache lines.

## 2. Core Primitives
Hardware caching dynamics: Spatial locality, temporal locality, cache line invalidations, SoA vs AoS; B-Trees vs BSTs: Node sizing aligned to 64-byte cache lines and 4KB page boundaries, fan-out mechanics, node splitting, key search via SIMD vectorization.

## 3. Physical & Virtual Workbenches (BOM)
Hardware performance counter profiler (perf on Linux).

## 4. Primary Literature & Canonical Links
- **[Seminal Paper]** [Ulrich Drepper - What Every Programmer Should Know About Memory (Red Hat Technical Paper 2007)](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf)
- **[Textbook]** [Goetz Graefe - Modern B-Tree Techniques (Foundations and Trends in Databases)](https://dl.acm.org/doi/10.1561/1900000028)
- **[Seminal Paper]** [Rudolf Bayer & Edward M. McCreight - Organization and Maintenance of Large Ordered Indexes (B-Trees 1972)](https://link.springer.com/article/10.1007/BF00288683)
- **[Paper]** [Paul-Virak Khuong & Pat Morin - Array Layouts for Comparison-Based Searching (ACM JEA 2017)](https://arxiv.org/abs/1509.05053)

## 5. Standardized Milestone Projects
- **P23_1 (Alpha (Tactile))**: Cache-Line Access Visualizer — Visual tool mapping memory traversals and displaying cache hits vs. cache misses in real time.
- **P23_2 (Beta (Milestone))**: 64-Byte Cache-Conscious B-Tree — Implement a B-Tree in C/Rust with node sizing matched to 64-byte cache lines; benchmark vs binary trees.
- **P23_3 (Gamma (Capstone))**: SIMD-Accelerated Vector Scanner — Write a search engine in C using AVX2/NEON intrinsics scanning 8 keys per clock cycle without branching.
