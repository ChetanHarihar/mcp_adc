from mcpadc import MCP
import time

# Initialize MCP object for MCP3008 ADC (10-bit resolution, 8 channels)
adc_module = MCP(model="3008", v_ref=5.0) # v_ref can be 3.3 or 5.0

try:
    while True:
        # Read LDR value from channel 0
        ldr_channel = 0
        ldr_raw_value = adc_module.read_channel(ldr_channel)
        ldr_voltage = adc_module.convert_to_voltage(ldr_raw_value)

        print(f"LDR - Raw Value: {ldr_raw_value}, Voltage: {ldr_voltage:.3f}V")

        # Read gas sensor value from channel 1
        gas_channel = 1
        gas_raw_value = adc_module.read_channel(gas_channel)
        gas_voltage = adc_module.convert_to_voltage(gas_raw_value)

        print(f"Gas Sensor - Raw Value: {gas_raw_value}, Voltage: {gas_voltage:.3f}V")

        # Wait for 1 second before the next reading
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by the user.")
    adc_module.cleanup()