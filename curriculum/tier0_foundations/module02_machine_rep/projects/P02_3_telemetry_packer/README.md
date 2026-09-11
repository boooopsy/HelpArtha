# Binary Telemetry Bit-Packer (P02_3)

**Module:** Machine Representation, Bitwise Engines & IEEE 754 (`module02_machine_rep`)  
**Classification:** Gamma (Capstone)  

## 1. Project Objective
Implement a packed telemetry serializer in C encoding 3 sensor channels into a single 32-bit unsigned integer using bitfields.

## 2. Mental Model & Physical Analogy
An n-bit register is a circular odometer. Overflow cycles back to zero. Negative numbers are defined by shifting perspective on this wheel (Two's Complement). Floating point is scientific notation encoded in bitfields.

## 3. Bill of Materials / Tools
8-position DIP switch module with LED indicators, logic probe.
