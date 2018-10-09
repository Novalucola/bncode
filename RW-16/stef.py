"""
Code from:
https://www.raspberrypi-spy.co.uk/2013/10/analogue-sensors-on-the-raspberry-pi-using-an-mcp3008/
"""

#!/usr/bin/python
 
import spidev
import time
import os

# -- ADC units --
# The ADC is 10bit so it can report a range of numbers from 0 to 1023 (2 to the power of 10).
# A reading of 0 means the input is 0V and a reading of 1023 means the input is 3.3V

ADC_max_val = 1023
ADC_max_voltage = 3.3 # Unit volts

# Converts an ADC value to decimal percentage representation (1 <==> 100%)
def conv_ADC_to_percentage(val):
    return val / ADC_max_val

# Converts an ADC value to volts
def conv_ADC_to_volt(val):
    perc = conv_ADC_to_percentage(val)
    return perc * ADC_max_voltage
    pass


class MCP_chip:
    
    # Open SPI bus
    spi = spidev.SpiDev()
    
    # open will connect to the specified SPI device, opening /dev/spidev<bus>.<device>
    bus = 0     # SPI bus to connect to
    device = 0  # SPI device to connect to
    
    def __init__(self, bus = 0, device = 0):
        self.bus = bus
        self.device = device
    
    # Open SPI port
    def open(self):
        self.spi.open(self.bus, self.device)
    
    # Close SPI port
    def close(self):
        self.spi.close()

    # Change bus value
    def change_bus(self, bus):
        self.bus = bus
    
    # Change device value
    def change_device(self, device):
        self.device = bus
        
    def change_frequency(self, val):
        self.spi.max_speed_hz = val
        
    # Function to read SPI data from MCP3008 chip
    # Channel must be an integer 0-7
    def ReadChannel(self, channel):
        adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data



chip_0 = MCP_chip()
chip_0.open()
chip_0.change_frequency(1000000)

# Open SPI bus
#spi = spidev.SpiDev()
#spi.open(0,0)
#spi.max_speed_hz=1000000

# TODO testa frekvens (comm), 2 kHz vore bra
 
# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data
 

# Define sensor channels
light_channel = 0
temp_channel  = 1
 
# Define delay between readings
delay = 1

def freq_test():
    
    start = time.time()
    
    iters = 10**5
    
    for i in range(0, iters):
        light_level = chip_0.ReadChannel(light_channel)
        
    stop = time.time()
    
    dur = stop - start
    
    freq = iters / dur
    
    print("Duration (s): ", dur)
    print("Freq (Hz): \t  ", freq)    

freq_test()

"""

try:
    while True:
        
        # Read the light sensor data
        #light_level = ReadChannel(light_channel)
        light_level = chip_0.ReadChannel(light_channel)

        # Print out results
        print ("--------------------------------------------")
        print("Registered value : " +  str(light_level))


        # Wait before repeating loop
        time.sleep(delay)
finally:
    chip_0.close()
    
"""