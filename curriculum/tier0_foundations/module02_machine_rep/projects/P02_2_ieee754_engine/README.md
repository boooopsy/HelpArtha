# Software IEEE 754 Engine (P02_2)

**Module:** Machine Representation, Bitwise Engines & IEEE 754 (`module02_machine_rep`)  
**Classification:** Beta (Milestone)  

## 1. Project Objective
Parse 32 raw hex bits into sign, exponent, and mantissa in pure Python without float casting.

## 2. Mental Model & Physical Analogy
An n-bit register is a circular odometer. Overflow cycles back to zero. Negative numbers are defined by shifting perspective on this wheel (Two's Complement). Floating point is scientific notation encoded in bitfields.

## 3. Bill of Materials / Tools
8-position DIP switch module with LED indicators, logic probe.
