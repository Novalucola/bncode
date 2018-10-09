"""
https://gpiozero.readthedocs.io/en/stable/recipes.html
https://gpiozero.readthedocs.io/en/stable/installing.html
"""
from gpiozero import MCP3008
CE0 = 8
CE1 = 7
#MCP3008(channel=0)
#MCP3008(channel=0, device=0)
#MCP3008(channel=0, port=0, device=0)
#MCP3008(channel=0, select_pin=8) #CE0 GPIO8
#MCP3008(channel=0, select_pin=7) #CE1 GPIO7
#MCP3008(channel=0, clock_pin=11, mosi_pin=10, miso_pin=9, select_pin=8)

def readvoltage(device, chn):
  voltlevel = MCP3008(channel=chn, select_pin=device)
  return voltlevel

print(readvoltage(CE0, 0)) 