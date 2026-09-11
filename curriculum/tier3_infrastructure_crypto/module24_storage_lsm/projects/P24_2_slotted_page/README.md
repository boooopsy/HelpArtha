# Slotted-Page Storage Manager (P24_2)

**Module:** Storage Engines, Write-Ahead Logs & LSM-Trees (`module24_storage_lsm`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Implement a binary page manager in C with tuple slot offsets, frame pinning, and LRU page eviction.

## 2. Mental Model & Physical Analogy
Data stored only in memory will be lost if power fails. To guarantee durability, modifications must be written sequentially to a disk log before updating memory.

## 3. Bill of Materials / Tools
Raw block device / loopback mount with crash-simulation tooling.
