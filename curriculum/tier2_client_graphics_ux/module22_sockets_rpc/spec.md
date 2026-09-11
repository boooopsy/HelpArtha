# Module 22: Network Sockets, TCP/IP & Custom RPC Protocols

**Tier:** `tier2_client_graphics_ux`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Network programming connects systems via data streams. The OS handles buffering, packet ordering, and retransmissions under the hood.

## 2. Core Primitives
Transport layer fundamentals: TCP 3-way handshake, sequence numbers, sliding-window flow control, congestion control; I/O multiplexing: Non-blocking sockets (O_NONBLOCK), kernel event demultiplexing (epoll); binary framing protocols: Length-prefixed payloads, magic bytes, checksums, zero-copy serialization.

## 3. Physical & Virtual Workbenches (BOM)
Wireshark packet analyzer, local loopback network interface.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [W. Richard Stevens, Bill Fenner, Andrew M. Rudoff - UNIX Network Programming, Vol 1: Sockets API](http://www.unpbook.com/)
- **[Workbench]** [Brian 'Beej Jorgensen' Hall - Beej's Guide to Network Programming: Using Internet Sockets](https://beej.us/guide/bgnet/)
- **[Seminal Paper]** [Vinton G. Cerf & Robert E. Kahn - A Protocol for Packet Network Intercommunication (IEEE 1974)](https://ieeexplore.ieee.org/document/1097808)
- **[Specification]** [Jon Postel - RFC 793: Transmission Control Protocol (DARPA Internet Program Protocol Spec)](https://www.rfc-editor.org/rfc/rfc793)

## 5. Standardized Milestone Projects
- **P22_1 (Alpha (Tactile))**: Raw Packet Hex Decoder — Build a CLI utility that parses Ethernet, IPv4, and TCP headers from raw socket captures.
- **P22_2 (Beta (Milestone))**: High-Throughput Linux Epoll Server — Build an event-driven server in C using Linux epoll capable of handling 10,000 idle connections.
- **P22_3 (Gamma (Capstone))**: Binary RPC Wire Protocol & Engine — Design a binary protocol with varint encoding and CRC32 checks connecting your web panel to hardware.
