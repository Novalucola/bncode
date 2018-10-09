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
#import wiringpi2 as wiringpi
import time
#from gpiozero import MCP3008
import csv
import random
import datetime
logfile_name = "_testfile.csv"
simulatevoltage = True
logtofile = True
CE0 = 8
CE1 = 7


def write_to_log_file(data):
  fout = open(logfile_name, 'a')
  fout.write(data)
  fout.write("\n")
  fout.close()

def read(comment, device, chn):
  NowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
  if simulatevoltage:
    voltlevel =  random.uniform(1.5, 1.9)
  else:
    #voltlevel = MCP3008(channel=chn, select_pin=device)
    voltlevel =  random.uniform(1.5, 1.9)
  if logtofile:
    write_to_log_file(str(NowTime) + "," + device + "," + str(chn) + "," + str(voltlevel))
  print(NowTime, "[", comment, "] ", device, chn, voltlevel)
  
def switch(comment, device, pinbase, onoff):
  NowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
  #wiringpi.wiringPiSetup()
  #wiringpi.mcp23017Setup(pinbase,device)
  #wiringpi.pinMode(pinbase, 1)
  #wiringpi.digitalWrite(pinbase, onoff)
  print(NowTime, "[", comment, "] ", device, pinbase, onoff )

def endtest(comment):
  print("[", comment, "] ")

with open('test1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] == "Read":
          read(row[6], row[1], row[2])
        elif row[0] == "Switch":
          switch(row[6], row[1], row[2], row[3])
        elif row[0] == "End":
          endtest(row[6])
        time.sleep(int(row[4]))