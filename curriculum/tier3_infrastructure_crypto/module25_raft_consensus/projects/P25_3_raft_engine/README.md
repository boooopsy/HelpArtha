# Full Raft Consensus Engine (P25_3)

**Module:** Distributed Consensus, Logical Clocks & Raft (`module25_raft_consensus`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Implement the Raft protocol from scratch in Go or Rust, maintaining consistency through network splits.

## 2. Mental Model & Physical Analogy
Physical clocks drift across independent network nodes. Distributed systems must establish ordering using sequence numbers (logical clocks) and require majority quorums before confirming state.

## 3. Bill of Materials / Tools
Multi-container local Docker/Linux testbed for simulated network drops.
