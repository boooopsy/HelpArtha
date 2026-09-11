# Module 14: Virtual Memory, MMUs & Bare-Metal OS Kernel Development

**Tier:** `tier1_core_systems`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Virtual memory gives each application the illusion that it has exclusive access to the entire RAM space. The MMU dynamically translates these virtual addresses.

## 2. Core Primitives
Virtual vs physical addresses, 4KB page frames, multi-level page tables (Sv39, x86-64 4-level), PTEs (valid, read, write, execute flags); MMU, TLB, TLB shootdowns, page faults, demand paging; privilege rings (User vs Supervisor/Kernel), system call traps (ecall), context switching, TCBs.

## 3. Physical & Virtual Workbenches (BOM)
QEMU system emulator (qemu-system-riscv64 or qemu-system-x86_64).

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Remzi H. Arpaci-Dusseau & Andrea C. Arpaci-Dusseau - Operating Systems: Three Easy Pieces (OSTEP)](https://pages.cs.wisc.edu/~remzi/OSTEP/)
- **[Textbook]** [Robert Love - Linux Kernel Development (3rd Edition, Addison-Wesley)](https://www.amazon.com/Linux-Kernel-Development-Robert-Love/dp/0672329468)
- **[Workbench]** [OSDev Community - The OSDev Bare-Metal Operating System Development Wiki](https://wiki.osdev.org/)
- **[Seminal Paper]** [Peter J. Denning - The Working Set Model for Program Behavior (1968)](https://dl.acm.org/doi/10.1145/363095.363141)

## 5. Standardized Milestone Projects
- **P14_1 (Alpha (Tactile))**: Page Table Walker & TLB Cache — Build a standalone address translation engine in C parsing multi-level page tables with TLB.
- **P14_2 (Beta (Milestone))**: QEMU Bare-Metal Kernel — Write a minimal OS kernel in C and assembly running on QEMU that configures MMU and timer interrupts.
- **P14_3 (Gamma (Capstone))**: Demand-Paging Fault Handler — Implement a page-fault exception handler that dynamically allocates and maps physical pages.
