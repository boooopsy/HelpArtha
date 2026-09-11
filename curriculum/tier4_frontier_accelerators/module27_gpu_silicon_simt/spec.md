# Module 27: GPU Silicon Architecture, SIMD/SIMT & Parallel Kernels

**Tier:** `tier4_frontier_accelerators`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>A CPU core is a fast, versatile processor handling complex serial tasks. A GPU consists of thousands of lightweight execution units operating in lock-step to process large arrays of data in parallel.

## 2. Core Primitives
GPU hardware topology: Latency vs throughput architectures, streaming multiprocessors (SMs), high-bandwidth memory (HBM), PCIe bottlenecks; SIMT model: Grids, thread blocks, warps (32 threads lock-step), warp divergence, coalesced memory access; GEMM optimization: 2D shared-memory tiling, register reuse, arithmetic intensity, Roofline Model.

## 3. Physical & Virtual Workbenches (BOM)
NVIDIA GPU / Apple Silicon with Metal / WebGPU execution capabilities.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [David B. Kirk & Wen-mei W. Hwu - Programming Massively Parallel Processors: A Hands-on Approach (PMPP 4th Edition)](https://www.elsevier.com/books/programming-massively-parallel-processors/kirk/978-0-323-91231-0)
- **[Specification]** [NVIDIA Corporation - CUDA C++ Programming Guide (Version 12.x)](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- **[Seminal Paper]** [Vasily Volkov & James W. Demmel - Benchmarking GPUs to Tune Dense Linear Algebra (SC 2008)](https://people.eecs.berkeley.edu/~volkov/volkov08-SC08.pdf)

## 5. Standardized Milestone Projects
- **P27_1 (Alpha (Tactile))**: Warp Divergence Simulator — Build a cycle simulator demonstrating execution serialization when threads take divergent branch paths.
- **P27_2 (Beta (Milestone))**: Hardware Roofline Benchmark Engine — Build a tool measuring arithmetic intensity determining compute vs. memory bounds.
- **P27_3 (Gamma (Capstone))**: 2D Tiled Shared-Memory GEMM Kernel — Write an optimized matrix multiplication kernel in CUDA/WebGPU achieving 8x speedup over naive baselines.
