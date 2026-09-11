# Module 02: Machine Representation, Bitwise Engines & IEEE 754

**Tier:** `tier0_foundations`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>An n-bit register is a circular odometer. Overflow cycles back to zero. Negative numbers are defined by shifting perspective on this wheel (Two's Complement). Floating point is scientific notation encoded in bitfields.

## 2. Core Primitives
Positional bases (2, 10, 16); Two's complement integer wheel, MSB as -2^(N-1), sign extension, overflow/underflow, arithmetic vs logical shifts; bitwise operations (&, |, ^, ~), bit clearing, toggling, power-of-two checks; IEEE 754 single precision: sign, biased exponent, mantissa, subnormals, NaNs.

## 3. Physical & Virtual Workbenches (BOM)
8-position DIP switch module with LED indicators, logic probe.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Henry S. Warren Jr. - Hacker's Delight (2nd Edition, Addison-Wesley)](https://hackersdelight.org/)
- **[Paper]** [William Kahan - Lecture Notes on the Status of IEEE 754 Floating-Point Standard](https://people.eecs.berkeley.edu/~wkahan/ieee754status/754story.html)
- **[Seminal Paper]** [David Goldberg - What Every Computer Scientist Should Know About Floating-Point Arithmetic (1991)](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)
- **[Simulator]** [H. Schmidt - IEEE-754 Interactive Single/Double Precision Float Converter](https://www.h-schmidt.net/FloatConverter/IEEE754.html)

## 5. Standardized Milestone Projects
- **P02_1 (Alpha (Tactile))**: Radial Two's Complement Dial — Interactive visualizer mapping integer overflows and sign flips on a circular dial.
- **P02_2 (Beta (Milestone))**: Software IEEE 754 Engine — Parse 32 raw hex bits into sign, exponent, and mantissa in pure Python without float casting.
- **P02_3 (Gamma (Capstone))**: Binary Telemetry Bit-Packer — Implement a packed telemetry serializer in C encoding 3 sensor channels into a single 32-bit unsigned integer using bitfields.
