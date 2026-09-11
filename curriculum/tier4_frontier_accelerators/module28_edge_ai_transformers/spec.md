# Module 28: Edge AI Devices, Quantized Transformers & Silicon Inference

**Tier:** `tier4_frontier_accelerators`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>A transformer model is a sequence of matrix operations. Text generation involves multiplying input vectors by weight matrices. By quantizing weights from 32-bit floats to 8-bit integers, models can run on microcontrollers.

## 2. Core Primitives
Transformer mechanics: Scaled dot-product attention, multi-head attention, RoPE, RMSNorm, residual connections; quantization systems: FP32 to INT8 (r = S * (q - Z)), symmetric quantization, dynamic range scaling; inference optimization: Autoregressive token generation loops, KV caches, streaming tokens to hardware displays.

## 3. Physical & Virtual Workbenches (BOM)
ESP32-S3 / RP2040 microcontroller board with 8MB+ flash, SSD1306 OLED, USB-C power, custom 3D printed enclosure from M11.

## 4. Primary Literature & Canonical Links
- **[Seminal Paper]** [Tri Dao et al. - FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness (NeurIPS 2022)](https://arxiv.org/abs/2205.14135)
- **[Seminal Paper]** [Ashish Vaswani et al. - Attention Is All You Need (Transformer Architecture, NeurIPS 2017)](https://arxiv.org/abs/1706.03762)
- **[Workbench]** [Georgi Gerganov et al. - llama.cpp: High-Performance On-Device LLM Inference in Pure C/C++](https://github.com/ggerganov/llama.cpp)
- **[Seminal Paper]** [Tim Dettmers et al. - LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale (NeurIPS 2022)](https://arxiv.org/abs/2208.07339)

## 5. Standardized Milestone Projects
- **P28_1 (Alpha (Tactile))**: Standalone Transformer Inference Engine — Write an inference engine in pure C that loads raw binary weights and executes forward passes.
- **P28_2 (Beta (Milestone))**: INT8 Tensor Quantization Tool — Build a converter that quantizes FP32 transformer weights into INT8 with per-channel scaling factors.
- **P28_3 (Gamma (Capstone))**: The Physical Mini-AI Device — Flash your quantized transformer engine onto an embedded microcontroller (ESP32-S3 / RP2040) housed in your custom 3D-printed enclosure from M11, running real-time on-device inference displayed on an integrated OLED screen.
