# Module 25: Distributed Consensus, Logical Clocks & Raft

**Tier:** `tier3_infrastructure_crypto`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Physical clocks drift across independent network nodes. Distributed systems must establish ordering using sequence numbers (logical clocks) and require majority quorums before confirming state.

## 2. Core Primitives
Distributed time: Clock drift, network partitions, split-brain, Lamport Timestamps, Vector Clocks; Raft consensus protocol: Roles (Follower, Candidate, Leader), randomized election timeouts, term numbers, log replication (AppendEntries), log matching invariant, commit index advancement, safety invariants.

## 3. Physical & Virtual Workbenches (BOM)
Multi-container local Docker/Linux testbed for simulated network drops.

## 4. Primary Literature & Canonical Links
- **[Seminal Paper]** [Diego Ongaro & John Ousterhout - In Search of an Understandable Consensus Algorithm (Raft, USENIX ATC 2014)](https://raft.github.io/raft.pdf)
- **[Seminal Paper]** [Leslie Lamport - Time, Clocks, and the Ordering of Events in a Distributed System (1978)](https://lamport.azurewebsites.net/pubs/time-clocks.pdf)
- **[Seminal Paper]** [Leslie Lamport - Paxos Made Simple (2001)](https://lamport.azurewebsites.net/pubs/paxos-simple.pdf)
- **[Seminal Paper]** [Eric Brewer - Towards Robust Distributed Systems (CAP Theorem Keynote, ACM PODC 2000)](https://people.eecs.berkeley.edu/~brewer/cs262b-2004/PODC-keynote.pdf)

## 5. Standardized Milestone Projects
- **P25_1 (Alpha (Tactile))**: Network Chaos Simulation Workbench — Build a simulated distributed test harness injecting configurable latency, packet drops, and partitions.
- **P25_2 (Beta (Milestone))**: Vector Clock Causal Message Broker — Implement a multi-node messaging system tracking causal history and detecting write conflicts.
- **P25_3 (Gamma (Capstone))**: Full Raft Consensus Engine — Implement the Raft protocol from scratch in Go or Rust, maintaining consistency through network splits.
