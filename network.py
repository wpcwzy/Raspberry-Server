import os
import time

port=serial.Serial("/dev/ttyAMA0",9600)

print("Serial Inited")

def scan():
    while(1):
        try:
            result=os.system("ping localhost -c 4")
            print result
            time.sleep(60)
        except KeyboardInterrupt:
            print"Keyboard"
            exit(0)

if __name__=="__main__":
    scan()