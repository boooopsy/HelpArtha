# 2D Tiled Shared-Memory GEMM Kernel (P27_3)

**Module:** GPU Silicon Architecture, SIMD/SIMT & Parallel Kernels (`module27_gpu_silicon_simt`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Write an optimized matrix multiplication kernel in CUDA/WebGPU achieving 8x speedup over naive baselines.

## 2. Mental Model & Physical Analogy
A CPU core is a fast, versatile processor handling complex serial tasks. A GPU consists of thousands of lightweight execution units operating in lock-step to process large arrays of data in parallel.

## 3. Bill of Materials / Tools
NVIDIA GPU / Apple Silicon with Metal / WebGPU execution capabilities.
