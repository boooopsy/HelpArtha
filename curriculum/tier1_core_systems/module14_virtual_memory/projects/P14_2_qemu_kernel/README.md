# QEMU Bare-Metal Kernel (P14_2)

**Module:** Virtual Memory, MMUs & Bare-Metal OS Kernel Development (`module14_virtual_memory`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Write a minimal OS kernel in C and assembly running on QEMU that configures MMU and timer interrupts.

## 2. Mental Model & Physical Analogy
Virtual memory gives each application the illusion that it has exclusive access to the entire RAM space. The MMU dynamically translates these virtual addresses.

## 3. Bill of Materials / Tools
QEMU system emulator (qemu-system-riscv64 or qemu-system-x86_64).
