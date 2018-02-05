# -*- coding:utf-8 -*-
import serial

port=serial.Serial("/dev/ttyAMA0",9600)

print("Serial Inited")
port.write("Test")
source=port.read()
print source

print("Finished")