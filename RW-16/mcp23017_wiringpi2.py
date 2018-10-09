# -*- coding: utf-8 -*-
"""
Install wiringpi:
  https://raspi.tv/how-to-install-wiringpi2-for-python-on-the-raspberry-pi#install
Code 1:
  https://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian
Code 2:
  https://raspi.tv/2013/using-the-mcp23017-port-expander-with-wiringpi2-to-give-you-16-new-gpio-ports-part-3
"""

# -*- coding: utf-8 -*-
"""
Install wiringpi:
  https://raspi.tv/how-to-install-wiringpi2-for-python-on-the-raspberry-pi#install
Code 1:
  https://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian
Code 2:
  https://raspi.tv/2013/using-the-mcp23017-port-expander-with-wiringpi2-to-give-you-16-new-gpio-ports-part-3
"""

import wiringpi
from time import sleep

pin_base = 65       # lowest available starting number is 65
i2c_addr = 0x20     # A0, A1, A2 pins all wired to GND

wiringpi.wiringPiSetup()                    # initialise wiringpi
wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address

wiringpi.pinMode(65, 1)         # sets GPA0 to output
wiringpi.digitalWrite(65, 0)    # sets GPA0 to 0 (0V, off)

counter = 0
try:
    while True:
        
        wiringpi.digitalWrite(65, 1) # sets port GPA1 to 1 (3V3, on)
        counter = counter + 1       
        print("set ON", str(counter))
        sleep(1)
        wiringpi.digitalWrite(65, 0) # sets port GPA1 to 0 (0V, off)
        print("set OFF", str(counter))
        sleep(1)


finally:
    wiringpi.digitalWrite(65, 0) # sets port GPA1 to 0 (0V, off)
    wiringpi.pinMode(65, 0)      # sets GPIO GPA1 back to input Mode
    # GPB7 is already an input, so no need to change anything