# Module 07: POSIX OS Mechanics, System Streams & Shell Tools

**Tier:** `tier0_foundations`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>In Unix, everything is a stream of bytes accessible via an integer file descriptor. Software programs are modular components connected with pipes.

## 2. Core Primitives
Standard streams (stdin 0, stdout 1, stderr 2), file descriptor tables, redirection, pipes; process lifecycle, fork() address cloning, execve() replacement, waitpid(), zombies/orphans, POSIX signals (SIGINT, SIGTERM, SIGKILL); inodes, file offsets, system calls (open, read, write, close, lseek).

## 3. Physical & Virtual Workbenches (BOM)
Linux terminal environment, USB serial debug cable.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Brian W. Kernighan & Rob Pike - The UNIX Programming Environment (Prentice Hall)](https://cm.bell-labs.com/cm/cs/upe/)
- **[Textbook]** [W. Richard Stevens & Stephen A. Rago - Advanced Programming in the UNIX Environment (APUE 3rd Edition)](http://www.apuebook.com/)
- **[Textbook]** [William E. Shotts Jr. - The Linux Command Line: A Complete Introduction (No Starch Press)](https://linuxcommand.org/tlcl.php)
- **[Seminal Paper]** [Dennis M. Ritchie & Ken Thompson - The UNIX Time-Sharing System (1974)](https://dl.acm.org/doi/10.1145/361011.361061)

## 5. Standardized Milestone Projects
- **P07_1 (Alpha (Tactile))**: Stream Redirection Sandbox — CLI workbench visualizing data flowing through file descriptors and kernel pipe buffers.
- **P07_2 (Beta (Milestone))**: Custom POSIX Command-Line Shell — Build a Unix shell in C supporting execution, multi-stage pipelines (cmd1 | cmd2), and redirects.
- **P07_3 (Gamma (Capstone))**: Streaming Grep & WC Clone — Build a high-throughput stream processing tool using low-level POSIX system calls.
