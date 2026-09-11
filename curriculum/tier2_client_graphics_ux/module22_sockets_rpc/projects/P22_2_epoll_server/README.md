# High-Throughput Linux Epoll Server (P22_2)

**Module:** Network Sockets, TCP/IP & Custom RPC Protocols (`module22_sockets_rpc`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Build an event-driven server in C using Linux epoll capable of handling 10,000 idle connections.

## 2. Mental Model & Physical Analogy
Network programming connects systems via data streams. The OS handles buffering, packet ordering, and retransmissions under the hood.

## 3. Bill of Materials / Tools
Wireshark packet analyzer, local loopback network interface.
