# Page Table Walker & TLB Cache (P14_1)

**Module:** Virtual Memory, MMUs & Bare-Metal OS Kernel Development (`module14_virtual_memory`)  
**Classification:** Alpha (Tactile)  

## 1. Project Objective
Build a standalone address translation engine in C parsing multi-level page tables with TLB.

## 2. Mental Model & Physical Analogy
Virtual memory gives each application the illusion that it has exclusive access to the entire RAM space. The MMU dynamically translates these virtual addresses.

## 3. Bill of Materials / Tools
QEMU system emulator (qemu-system-riscv64 or qemu-system-x86_64).
