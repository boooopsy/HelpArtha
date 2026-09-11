# Bit-Banged I2C Sensor Driver (P12_1)

**Module:** Embedded Firmware, Microcontrollers & Hardware Buses (`module12_embedded_firmware`)  
**Classification:** Alpha (Tactile)  

## 1. Project Objective
Read environmental sensor data by manually driving GPIO pins high/low in C without libraries.

## 2. Mental Model & Physical Analogy
A microcontroller is a CPU connected directly to physical pins via Memory-Mapped I/O (MMIO). Writing to a specific address toggles an external pin between 0V and 3.3V.

## 3. Bill of Materials / Tools
Raspberry Pi Pico (RP2040) / ESP32-S3 board, logic analyzer (8-channel 24MHz), SSD1306 SPI OLED display, BME280 I2C sensor.
