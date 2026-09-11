# Module 08: Systems C Programming, Memory Topology & Pointers

**Tier:** `tier1_core_systems`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Memory is a single-dimensional array of 8-bit cubbies. A pointer is an index into that array. Dereferencing is opening the cubby at that index to read or write its contents.

## 2. Core Primitives
Flat byte address space, pointer dereferencing (*p), address-of (&x), void pointers, typed pointer arithmetic, function pointers; stack frame layouts (rbp, rsp), dynamic heap allocation (malloc/free), chunk headers, fragmentation; struct padding, natural word alignment, cache lines (64 bytes), UB, use-after-free, double-free.

## 3. Physical & Virtual Workbenches (BOM)
Memory layout diagram chart, hardware address decoder simulator.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Brian W. Kernighan & Dennis M. Ritchie - The C Programming Language (ANSI C, 2nd Edition)](https://www.amazon.com/Programming-Language-2nd-Brian-Kernighan/dp/0131103628)
- **[Textbook]** [Peter van der Linden - Expert C Programming: Deep C Secrets (SunSoft Press)](https://www.amazon.com/Expert-Programming-Peter-van-Linden/dp/0131774298)
- **[Textbook]** [Randal E. Bryant & David R. O'Hallaron - Computer Systems: A Programmer's Perspective (CS:APP 3rd Edition)](http://csapp.cs.cmu.edu/)
- **[Workbench]** [Brian 'Beej Jorgensen' Hall - Beej's Guide to C Programming](https://beej.us/guide/bgc/)

## 5. Standardized Milestone Projects
- **P08_1 (Alpha (Tactile))**: Visual Memory Hex Dumper — Build a C debugging utility that inspects memory blocks, printing hex representations and endianness.
- **P08_2 (Beta (Milestone))**: Byte-Aligned Slab/Arena Allocator — Write a custom arena allocator in C featuring out-of-memory guards and reset capabilities.
- **P08_3 (Gamma (Capstone))**: Cache-Stride Latency Benchmark — Build a diagnostic harness in C measuring latency cliffs as stride lengths exceed 64-byte lines.
