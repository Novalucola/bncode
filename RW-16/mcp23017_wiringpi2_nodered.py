# -*- coding: utf-8 -*-


"""
Install wiringpi:
  https://raspi.tv/how-to-install-wiringpi2-for-python-on-the-raspberry-pi#install
Code 1:
  https://raspi.tv/2013/how-to-use-wiringpi2-for-python-on-the-raspberry-pi-in-raspbian
Code 2:
  https://raspi.tv/2013/using-the-mcp23017-port-expander-with-wiringpi2-to-give-you-16-new-gpio-ports-part-3
"""


import sys
# import wiringpi2 as wiringpi
import datetime
pinbase = ""
inpin = sys.argv[1]
onoff = sys.argv[2]
#print(inpin)
if inpin == str(1):
  pinbase = 73
elif inpin == str(2):
  pinbase = 74
elif inpin == str(3):
  pinbase = 75
elif inpin == str(4):
  pinbase = 76
elif inpin == str(5):
  pinbase = 77
elif inpin == str(6):
  pinbase = 78
elif inpin == str(7):
  pinbase = 79
elif inpin == str(8):
  pinbase = 80
elif inpin == str(9):
  pinbase = 65
elif inpin == str(10):
  pinbase = 66
elif inpin == str(11):
  pinbase = 67
elif inpin == str(12):
  pinbase = 68
elif inpin == str(13):
  pinbase = 69
elif inpin == str(14):
  pinbase = 70
elif inpin == str(15):
  pinbase = 41
elif inpin == str(16):
  pinbase = 72
  

print(pinbase, onoff)




NowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
#wiringpi.wiringPiSetup()
#wiringpi.mcp23017Setup(65,0x20)

#wiringpi.pinMode(pinbase, 1)
#wiringpi.digitalWrite(pinbase, onoff)
#print(NowTime, pinbase, onoff )

# Call: 65 1     For HIGH
# Call: 65 0     For LOW