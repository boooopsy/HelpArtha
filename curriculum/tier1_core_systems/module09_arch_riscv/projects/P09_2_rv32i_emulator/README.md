# Cycle-Accurate RV32I Software CPU Emulator (P09_2)

**Module:** Computer Architecture & Assembly (RISC-V RV32I) (`module09_arch_riscv`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Build an emulator in C supporting the 37 base RV32I instructions and 64KB of RAM.

## 2. Mental Model & Physical Analogy
A CPU is a finite state machine: it reads a 32-bit number pointed to by a program counter, flips internal routing switches based on that number, passes values through an ALU, and increments the counter.

## 3. Bill of Materials / Tools
RISC-V green card instruction reference, Venus / RARS simulator.
