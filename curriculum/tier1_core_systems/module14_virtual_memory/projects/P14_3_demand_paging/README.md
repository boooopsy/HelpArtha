# Demand-Paging Fault Handler (P14_3)

**Module:** Virtual Memory, MMUs & Bare-Metal OS Kernel Development (`module14_virtual_memory`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Implement a page-fault exception handler that dynamically allocates and maps physical pages.

## 2. Mental Model & Physical Analogy
Virtual memory gives each application the illusion that it has exclusive access to the entire RAM space. The MMU dynamically translates these virtual addresses.

## 3. Bill of Materials / Tools
QEMU system emulator (qemu-system-riscv64 or qemu-system-x86_64).
