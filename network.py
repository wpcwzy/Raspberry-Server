import os
import time
import serial

port=serial.Serial("/dev/ttyAMA0",9600)

print("Serial Inited")

def scan():
    while(1):
        try:
            result=os.system("ping www.baidu.com -c 4")
            print result
            if result!=0:
                print "Main Network Faild!!!\nSwitch to secondary network!!!"
                port.write("~")
                port.write("~")
                port.write("~")
                port.write("~")
                port.write("~")
            time.sleep(60)
        except KeyboardInterrupt:
            print"Keyboard"
            exit(0)

if __name__=="__main__":
    scan()