# -*- coding: utf-8 -*-
"""
For MCP3008:
  https://gpiozero.readthedocs.io/en/stable/installing.html

Install wiringpi:
  https://raspi.tv/how-to-install-wiringpi2-for-python-on-the-raspberry-pi#install
Code 1:
  https://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian
Code 2:
  https://raspi.tv/2013/using-the-mcp23017-port-expander-with-wiringpi2-to-give-you-16-new-gpio-ports-part-3
"""
import wiringpi2 as wiringpi
from time import sleep
from gpiozero import MCP3008
CE0 = 8
CE1 = 7


def readvoltage(device, chn):
  voltlevel = MCP3008(channel=chn, select_pin=device)
  return voltlevel

def runswitch(deviceaddr, pinswitch, chn, readaddr):
  pin_base = pinstart       # lowest available starting number is 65
  i2c_addr = deviceaddr     # 0x20    A0, A1, A2 pins all wired to GND

  wiringpi.wiringPiSetup()                    # initialise wiringpi
  wiringpi.mcp23017Setup(pin_base,i2c_addr)   # set up the pins and i2c address

  wiringpi.pinMode(pinswitch, 1)         # sets GPA0 to output
  sleep(0.5)
  print(readvoltage(readaddr, chn))
  wiringpi.digitalWrite(pinswitch, 0)    # sets GPA0 to 0 (0V, off)



  wiringpi.pinMode(pinswitch, 0)      # sets GPIO GPA1 back to input Mode

chn = 0
for pinbase in range(65, 73):

  runswitch("0x20", pinbase, chn, 8)
  chn = chn + 1

chn = 0
for pinbase in range(73, 81):

  runswitch("0x20", pinbase, chn)
  chn = chn + 1


 