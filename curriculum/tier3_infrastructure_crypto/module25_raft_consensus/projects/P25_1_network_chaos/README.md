# Network Chaos Simulation Workbench (P25_1)

**Module:** Distributed Consensus, Logical Clocks & Raft (`module25_raft_consensus`)  
**Classification:** Alpha (Tactile)  

## 1. Project Objective
Build a simulated distributed test harness injecting configurable latency, packet drops, and partitions.

## 2. Mental Model & Physical Analogy
Physical clocks drift across independent network nodes. Distributed systems must establish ordering using sequence numbers (logical clocks) and require majority quorums before confirming state.

## 3. Bill of Materials / Tools
Multi-container local Docker/Linux testbed for simulated network drops.
