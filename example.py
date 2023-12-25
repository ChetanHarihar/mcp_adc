from mcpadc import MCP  # Import the MCP class from the provided module
import RPi.GPIO as GPIO  # Import the RPi.GPIO module for GPIO operations
import time  # Import the time module for time-related functions

# Initialize MCP object for MCP3008 ADC (10-bit resolution, 8 channels)
adc_module = MCP(model="3008", v_ref = 5.0) # v_ref can be 3.3 or 5.0

try:
    while True:
        # Read LDR value from channel 0
        ldr_channel = 0
        GPIO.output(adc_module.CS_ADC, GPIO.LOW)
        ldr_raw_value = adc_module.read_channel(ldr_channel)  # Read raw ADC value from LDR channel
        GPIO.output(adc_module.CS_ADC, GPIO.HIGH)
        ldr_voltage = round(adc_module.convert_to_voltage(ldr_raw_value), 2)  # Convert raw value to voltage and round to 2 decimal places

        print(f"LDR - Raw Value: {ldr_raw_value}, Voltage: {ldr_voltage:.3f}V")

        # Read gas sensor value from channel 1
        gas_sen_channel = 1
        GPIO.output(adc_module.CS_ADC, GPIO.LOW)
        gas_raw_value = adc_module.read_channel(gas_sen_channel)  # Read raw ADC value from gas_sen1 channel
        GPIO.output(adc_module.CS_ADC, GPIO.HIGH)
        gas_voltage = round(adc_module.convert_to_voltage(gas_sen1_raw_value), 2)  # Convert raw value to voltage and round to 2 decimal places

        print(f"Gas Sensor - Raw Value: {gas_raw_value}, Voltage: {gas_voltage:.3f}V")

        # Wait for 1 second before the next reading
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by the user.")
    adc_module.cleanup()