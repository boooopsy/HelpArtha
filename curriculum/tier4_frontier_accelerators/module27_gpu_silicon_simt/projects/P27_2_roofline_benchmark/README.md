# Hardware Roofline Benchmark Engine (P27_2)

**Module:** GPU Silicon Architecture, SIMD/SIMT & Parallel Kernels (`module27_gpu_silicon_simt`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Build a tool measuring arithmetic intensity determining compute vs. memory bounds.

## 2. Mental Model & Physical Analogy
A CPU core is a fast, versatile processor handling complex serial tasks. A GPU consists of thousands of lightweight execution units operating in lock-step to process large arrays of data in parallel.

## 3. Bill of Materials / Tools
NVIDIA GPU / Apple Silicon with Metal / WebGPU execution capabilities.
