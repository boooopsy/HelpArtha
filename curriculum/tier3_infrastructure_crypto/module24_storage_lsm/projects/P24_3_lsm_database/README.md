# Zero-Dependency LSM-Tree Database (P24_3)

**Module:** Storage Engines, Write-Ahead Logs & LSM-Trees (`module24_storage_lsm`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Build a complete LSM-Tree engine featuring MemTables, SSTables, Bloom filters, and compaction.

## 2. Mental Model & Physical Analogy
Data stored only in memory will be lost if power fails. To guarantee durability, modifications must be written sequentially to a disk log before updating memory.

## 3. Bill of Materials / Tools
Raw block device / loopback mount with crash-simulation tooling.
