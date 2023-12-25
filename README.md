---

# MCP ADC Interface

## Introduction

This repository provides Python scripts to interface with MCP3004 and MCP3008 Analog-to-Digital Converters (ADCs) on Raspberry Pi. The main script, `mcpadc.py`, defines a class called `MCP` that simplifies reading analog values from specific channels and converting them to voltages.

Additionally, an example script (`example.py`) showcases the usage of the `MCP` class for reading values from sensors connected to MCP3008 channels. In this example, an LDR (Light Dependent Resistor) and a gas sensor are used to demonstrate the capabilities of the MCP ADC interface.

## Usage

1. **Install Required Packages:**

   Before running the scripts, make sure the necessary packages are installed on your Raspberry Pi.

   - Install `spidev` for SPI communication:
     ```bash
     sudo apt-get update
     sudo apt-get install python3-spidev
     ```

   - Install `RPi.GPIO` for GPIO operations:
     ```bash
     sudo apt-get install python3-rpi.gpio
     ```

2. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/mcp_adc.git
   cd mcp_adc
   ```

3. **Run the Example Script:**

   ```bash
   python example.py
   ```

   The script will prompt you to enter the MCP model (3004 or 3008) and the channel for sensor readings. It continuously reads and prints the raw values and corresponding voltages for an LDR and a gas sensor.

## Dependencies

- `spidev`: SPI communication library for Python
- `RPi.GPIO`: GPIO library for Raspberry Pi

Ensure these libraries are installed before running the scripts.

## Cleanup

The `MCP` class includes a `cleanup` method to release GPIO and SPI resources when the script is terminated.

---
