# -*- coding:utf-8 -*-
import serial
import time

port=serial.Serial("/dev/ttyAMA0",9600)

print("Serial Inited")

def personDetect():
    while(1):
        source=port.read()
        print source
        if source=="!":
            port.write("~")

if __name=="__main__":
    personDetect()