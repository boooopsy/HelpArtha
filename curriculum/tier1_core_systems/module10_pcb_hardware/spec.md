# Module 10: Hardware Prototyping: Breadboarding & PCB Layout

**Tier:** `tier1_core_systems`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>Code requires physical housing. Traces on a printed circuit board are zero-resistance wires; decoupling capacitors are local energy reservoirs placed adjacent to IC power pins to absorb switching noise.

## 2. Core Primitives
Schematic capture, power nets, decoupling capacitor placement (0.1uF ceramics adjacent to VDD pins), pull-ups on open-drain lines; PCB track widths vs current capacity, copper weight (1 oz/ft^2), continuous ground planes, trace impedance, DRC rules, soldering technique.

## 3. Physical & Virtual Workbenches (BOM)
Digital multimeter, soldering station, lead-free solder, flux pen, copper braid, ESD mat; RP2040 / ESP32-S3 breakouts, KiCad 8.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Paul Horowitz & Winfield Hill - The Art of Electronics (3rd Edition, Cambridge University Press)](https://artofelectronics.net/)
- **[Textbook]** [Forrest M. Mims III - Getting Started in Electronics (Master Publishing)](https://forrestmims.org/)
- **[Tool]** [Wayne Stambaugh et al. - KiCad EDA Official Schematic and PCB Layout Suite Documentation](https://www.kicad.org/)
- **[Textbook]** [Howard Johnson & Martin Graham - High-Speed Digital Design: A Handbook of Black Magic](https://www.amazon.com/High-Speed-Digital-Design-Handbook-Black/dp/0133957241)

## 5. Standardized Milestone Projects
- **P10_1 (Alpha (Tactile))**: LED Flashlight PCB — Design a simple 2-layer PCB in KiCad with switch, resistors, LEDs, and power routing; generate Gerbers.
- **P10_2 (Beta (Milestone))**: Custom Microcontroller Breakout Board — Lay out a custom board in KiCad for an RP2040/ESP32-S3 with USB-C, LDO, and ESD diodes.
- **P10_3 (Gamma (Capstone))**: Physical Assembly & Solder Smoke-Test — Solder and assemble your custom PCB, verify rail voltages, and flash a blink firmware.
