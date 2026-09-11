# Module 12: Embedded Firmware, Microcontrollers & Hardware Buses

**Tier:** `tier1_core_systems`  
**Status:** Verified Master Specification  

## 1. Concrete Mental Model
>A microcontroller is a CPU connected directly to physical pins via Memory-Mapped I/O (MMIO). Writing to a specific address toggles an external pin between 0V and 3.3V.

## 2. Core Primitives
MMIO registers, volatile pointers in C, direction registers, data registers; UART (asynchronous, framing, baud); I2C (synchronous, SDA/SCL, open-drain pull-ups, 7-bit addressing, ACK/NACK); SPI (synchronous, 4-wire MOSI/MISO/SCK/CS, CPOL/CPHA); hardware Interrupt Service Routines (ISRs).

## 3. Physical & Virtual Workbenches (BOM)
Raspberry Pi Pico (RP2040) / ESP32-S3 board, logic analyzer (8-channel 24MHz), SSD1306 SPI OLED display, BME280 I2C sensor.

## 4. Primary Literature & Canonical Links
- **[Textbook]** [Jack Ganssle - The Art of Designing Embedded Systems (Newnes)](http://www.ganssle.com/)
- **[Textbook]** [Jonathan W. Valvano - Embedded Systems: Real-Time Interfacing to ARM Cortex-M Microcontrollers](http://users.ece.utexas.edu/~valvano/)
- **[Specification]** [Raspberry Pi Ltd - RP2040 Microcontroller Datasheet & C/C++ SDK Manual](https://www.raspberrypi.com/documentation/microcontrollers/c_sdk.html)
- **[Specification]** [NXP Semiconductors - I2C-Bus Specification and User Manual (UM10204)](https://www.nxp.com/docs/en/user-guide/UM10204.pdf)

## 5. Standardized Milestone Projects
- **P12_1 (Alpha (Tactile))**: Bit-Banged I2C Sensor Driver — Read environmental sensor data by manually driving GPIO pins high/low in C without libraries.
- **P12_2 (Beta (Milestone))**: Interrupt-Driven Circular UART Driver — Build a UART driver using ring buffers streaming command packets without dropping bytes.
- **P12_3 (Gamma (Capstone))**: SPI OLED Graphics Engine — Build a bare-metal display driver in C drawing shapes, text, and bitmaps to an SSD1306 OLED over SPI.
