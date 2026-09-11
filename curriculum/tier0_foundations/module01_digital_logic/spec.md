# Module 01: Switching Mechanics, Digital Logic & Clocks

**Tier:** `tier0_foundations`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Current flows or is blocked. A NOT gate is an electromagnet pulling an iron contact away from an output line. A clock is an oscillator driving the heartbeat of silicon.

## 2. Core Primitives
SPDT relays, electromagnets, flyback diodes, pull-up/pull-down resistors, push-pull stages; TTL 7400-series gates (AND, OR, NOT, XOR); universal NAND logic; half-adders, ripple-carry adders, propagation delay; SR-latches, D-Flip-Flops, setup/hold times.

## 3. Physical & Virtual Workbenches (BOM)
Breadboard, 5V supply, Songle SRD-05VDC relays, 1N4148 diodes, 74HC08, 74HC32, 74HC04, 74HC86, 74HC74, NE555P timer, LEDs, resistors.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Charles Petzold - CODE: The Hidden Language of Computer Hardware and Software (2nd Edition)](https://www.charlespetzold.com/code/)
- **[Course]** [Ben Eater - Building an 8-bit Computer on Breadboards from Scratch](https://eater.net/8bit)
- **[Simulator]** [Paul Falstad - Full Interactive Analog & Digital Circuit Simulator](https://falstad.com/circuit/)
- **[Tool]** [H. Neemann - Digital: High-Performance Digital Logic Simulator & Circuit Workbench](https://github.com/hneemann/Digital)
- **[Seminal Paper]** [Claude E. Shannon - A Symbolic Analysis of Relay and Switching Circuits (MIT 1938)](https://www.cs.virginia.edu/~evans/greatworks/shannon38.pdf)

## 5. Standardized Milestone Projects
- **P01_1 (Alpha (Tactile))**: Relay Oscillator & Buzzer — Wire a physical relay feedback loop with a capacitor and flyback diode to create an audible oscillator.
- **P01_2 (Beta (Milestone))**: 4-Bit TTL Ripple-Carry Adder — Wire a discrete 4-bit adder on a breadboard with LED bus outputs and an overflow flag.
- **P01_3 (Gamma (Capstone))**: Edge-Triggered 8-Bit Register Bank — Construct an 8-bit register with manual tactile clocking, reset controls, and bus isolation.
