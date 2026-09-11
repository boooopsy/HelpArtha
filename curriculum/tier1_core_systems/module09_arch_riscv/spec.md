# Module 09: Computer Architecture & Assembly (RISC-V RV32I)

**Tier:** `tier1_core_systems`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>A CPU is a finite state machine: it reads a 32-bit number pointed to by a program counter, flips internal routing switches based on that number, passes values through an ALU, and increments the counter.

## 2. Core Primitives
Program Counter (PC), Register File (x0 hardwired to ground, x1 to x31), ALU, Control Unit, Fetch-Decode-Execute; RV32I ISA instruction formats (R, I, S, B, U, J-types), arithmetic, memory (lw, sw), branches (beq, bne), jumps (jal, jalr), standard ABI (a0-a7, ra, sp).

## 3. Physical & Virtual Workbenches (BOM)
RISC-V green card instruction reference, Venus / RARS simulator.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [David A. Patterson & John L. Hennessy - Computer Organization and Design: RISC-V Edition](https://www.elsevier.com/books/computer-organization-and-design-risc-v-edition/patterson/978-0-12-812275-4)
- **[Textbook]** [David Patterson & Andrew Waterman - The RISC-V Reader: An Open Architecture Atlas](http://www.riscvbook.com/)
- **[Specification]** [Krste Asanović et al. - The RISC-V Instruction Set Manual, Volume I: Unprivileged ISA](https://riscv.org/technical/specifications/)
- **[Simulator]** [Keyan Vakil - Venus: Web-Based RISC-V RV32I Architecture Simulator](https://venus.kvakil.me/)

## 5. Standardized Milestone Projects
- **P09_1 (Alpha (Tactile))**: Step-by-Step Register Visualizer — Interactive tool showing register transformations and PC jumps during assembly execution.
- **P09_2 (Beta (Milestone))**: Cycle-Accurate RV32I Software CPU Emulator — Build an emulator in C supporting the 37 base RV32I instructions and 64KB of RAM.
- **P09_3 (Gamma (Capstone))**: Hand-Coded Assembly Quicksort — Write an in-place quicksort in pure RISC-V assembly and verify execution on your emulator.
