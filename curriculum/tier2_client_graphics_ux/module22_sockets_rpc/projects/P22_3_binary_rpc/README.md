# Binary RPC Wire Protocol & Engine (P22_3)

**Module:** Network Sockets, TCP/IP & Custom RPC Protocols (`module22_sockets_rpc`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Design a binary protocol with varint encoding and CRC32 checks connecting your web panel to hardware.

## 2. Mental Model & Physical Analogy
Network programming connects systems via data streams. The OS handles buffering, packet ordering, and retransmissions under the hood.

## 3. Bill of Materials / Tools
Wireshark packet analyzer, local loopback network interface.
