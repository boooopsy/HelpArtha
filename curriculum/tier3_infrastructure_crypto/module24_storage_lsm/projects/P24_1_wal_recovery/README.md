# Append-Only WAL Crash Recovery Engine (P24_1)

**Module:** Storage Engines, Write-Ahead Logs & LSM-Trees (`module24_storage_lsm`)  
**Classification:** Alpha (Tactile)  

## 1. Project Objective
Build a logging system that recovers an in-memory database state after a SIGKILL.

## 2. Mental Model & Physical Analogy
Data stored only in memory will be lost if power fails. To guarantee durability, modifications must be written sequentially to a disk log before updating memory.

## 3. Bill of Materials / Tools
Raw block device / loopback mount with crash-simulation tooling.
