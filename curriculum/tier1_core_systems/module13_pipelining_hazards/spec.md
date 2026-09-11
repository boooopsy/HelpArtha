# Module 13: Pipelined Microarchitecture, Hazards & Branch Prediction

**Tier:** `tier1_core_systems`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Pipelining is a car assembly line. If a worker downstream waits for a part being manufactured upstream, the line stalls unless parts are forwarded across stations.

## 2. Core Primitives
Classic 5-stage RISC pipeline (IF, ID, EX, MEM, WB); hazards: Structural, Data (RAW, WAR), Control (branches); pipeline stalls (NOP bubbles), data forwarding/bypassing; branch prediction: 1-bit/2-bit saturating counters, branch target buffers (BTB).

## 3. Physical & Virtual Workbenches (BOM)
Pipeline timing spreadsheet simulator, cycle-accurate instruction trace visualizer.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [John L. Hennessy & David A. Patterson - Computer Architecture: A Quantitative Approach (6th Edition)](https://www.elsevier.com/books/computer-architecture/hennessy/978-0-12-811905-1)
- **[Seminal Paper]** [Robert M. Tomasulo - An Efficient Algorithm for Exploiting Multiple Arithmetic Units (IBM 1967)](https://ieeexplore.ieee.org/document/5392028)
- **[Seminal Paper]** [Scott McFarling - Combining Branch Predictors (Digital WRL Technical Note 1993)](https://www.hpl.hp.com/techreports/Compaq-DEC/WRL-TN-36.pdf)

## 5. Standardized Milestone Projects
- **P13_1 (Alpha (Tactile))**: Pipeline Hazard Visualizer — Interactive diagram illustrating instruction bubbles and data forwarding paths across cycles.
- **P13_2 (Beta (Milestone))**: 5-Stage Pipelined RV32I Simulator — Extend the M09 emulator into a 5-stage pipelined simulator with hazard forwarding.
- **P13_3 (Gamma (Capstone))**: Branch Prediction Performance Harness — Implement a 2-bit saturating counter simulator and demonstrate throughput collapse.
