# Vector Clock Causal Message Broker (P25_2)

**Module:** Distributed Consensus, Logical Clocks & Raft (`module25_raft_consensus`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Implement a multi-node messaging system tracking causal history and detecting write conflicts.

## 2. Mental Model & Physical Analogy
Physical clocks drift across independent network nodes. Distributed systems must establish ordering using sequence numbers (logical clocks) and require majority quorums before confirming state.

## 3. Bill of Materials / Tools
Multi-container local Docker/Linux testbed for simulated network drops.
