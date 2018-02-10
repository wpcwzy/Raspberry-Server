import time
import serial
port=serial.Serial("/dev/ttyAMA0",9600)

print("Serial Inited")

def timer():
    timeNow=time.localtime()
    hour=timeNow.tm_hour
    if hour>=22 or hour<=7:
        port.write("^")
    else:
        port.write("|")
    time.sleep(60)

if __name__=="__main__":
    timer()