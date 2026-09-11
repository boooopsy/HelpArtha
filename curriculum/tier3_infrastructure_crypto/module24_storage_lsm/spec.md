# Module 24: Storage Engines, Write-Ahead Logs & LSM-Trees

**Tier:** `tier3_infrastructure_crypto`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Data stored only in memory will be lost if power fails. To guarantee durability, modifications must be written sequentially to a disk log before updating memory.

## 2. Core Primitives
Durability mechanics: Flash block erase physics, sequential vs random I/O, write amplification, kernel buffering and fsync(); LSM-Tree architecture: MemTable, WAL, SSTables, Bloom filters, multi-way merge background compaction.

## 3. Physical & Virtual Workbenches (BOM)
Raw block device / loopback mount with crash-simulation tooling.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Martin Kleppmann - Designing Data-Intensive Applications: The Big Ideas Behind Reliable Systems](https://dataintensive.net/)
- **[Seminal Paper]** [Patrick O'Neil, Edward O'Neil, Gerhard Weikum - The Log-Structured Merge-Tree (LSM-Tree 1996)](https://www.cs.umb.edu/~poneil/lsmtrie.pdf)
- **[Textbook]** [Jim Gray & Andreas Reuter - Transaction Processing: Concepts and Techniques (Morgan Kaufmann)](https://www.amazon.com/Transaction-Processing-Concepts-Techniques-Management/dp/1558601902)
- **[Workbench]** [Sanjay Ghemawat & Jeff Dean - LevelDB: A Fast and Lightweight Key-Value Storage Library](https://github.com/google/leveldb)

## 5. Standardized Milestone Projects
- **P24_1 (Alpha (Tactile))**: Append-Only WAL Crash Recovery Engine — Build a logging system that recovers an in-memory database state after a SIGKILL.
- **P24_2 (Beta (Milestone))**: Slotted-Page Storage Manager — Implement a binary page manager in C with tuple slot offsets, frame pinning, and LRU page eviction.
- **P24_3 (Gamma (Capstone))**: Zero-Dependency LSM-Tree Database — Build a complete LSM-Tree engine featuring MemTables, SSTables, Bloom filters, and compaction.
