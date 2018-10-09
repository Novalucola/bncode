# -*- coding: utf-8 -*-
import csv
import time
import datetime
def read(comment, device, chn):
  NowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
  print(NowTime, "[", comment, "] ", device, chn )
  
def switch(comment, device, pinbase, onoff):
  NowTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
  print(NowTime, "[", comment, "] ", device, pinbase, onoff )

def endtest(comment):
  print("[", comment, "] ")


with open("test1.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[0] == "Read":
          read(row[6], row[1], row[2])
        elif row[0] == "Switch":
          switch(row[6], row[1], row[2], row[3])
        elif row[0] == "End":
          endtest(row[6])
        time.sleep(int(row[4]))
