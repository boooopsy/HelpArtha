# INT8 Tensor Quantization Tool (P28_2)

**Module:** Edge AI Devices, Quantized Transformers & Silicon Inference (`module28_edge_ai_transformers`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Build a converter that quantizes FP32 transformer weights into INT8 with per-channel scaling factors.

## 2. Mental Model & Physical Analogy
A transformer model is a sequence of matrix operations. Text generation involves multiplying input vectors by weight matrices. By quantizing weights from 32-bit floats to 8-bit integers, models can run on microcontrollers.

## 3. Bill of Materials / Tools
ESP32-S3 / RP2040 microcontroller board with 8MB+ flash, SSD1306 OLED, USB-C power, custom 3D printed enclosure from M11.
