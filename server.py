#! /usr/bin/python
# -*- coding:utf-8 -*-#
import os
import time
import serial
import threading

log=open("server.log","a")

port=serial.Serial("/dev/ttyAMA0",9600)

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "Serial Inited"

log=open("server.log","a")
log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"  "+"Serial Inited.\n")
log.close()

def scan():
    while(1):
        try:
            result=os.system("ping www.baidu.com -c 4")
            print result
            if result!=0:
                print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print "Main Network Faild!!!\nSwitch to secondary network!!!"
                log=open("server.log","a")
                log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"  "+"Main Network Faild.\n")
                log.close()
                port.write("~")
                port.write("~")
                port.write("~")
                port.write("~")
                port.write("~")
            time.sleep(60)
        except KeyboardInterrupt:
            print"Keyboard"
            exit(0)

def timer():
    timeNow=time.localtime()
    hour=timeNow.tm_hour
    if hour>=22 or hour<=7:
        port.write("^")
        print "Mute"
    else:
        port.write("|")
        print "Normal"
    time.sleep(60)

def personDetect():
    while(1):
        source=port.read()
        print source
        if source=="!":
            port.write("~")
            log = open("server.log", "a")
            log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "  " + "Person Detected.\n")
            log.close()


if __name__=="__main__":
    MissionPerson=threading.Thread(target=personDetect,name="Person")
    MissionTimer=threading.Thread(target=timer,name="Time")
    MissionNetwork=threading.Thread(target=scan,name="Network")
    MissionNetwork.start()
    MissionPerson.start()
    MissionTimer.start()
    MissionTimer.setDaemon(True)
    MissionNetwork.setDaemon(True)
    MissionNetwork.join()
    MissionPerson.join()
    MissionTimer.join()
    log=open("server.log","a")
    log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"  "+"Threads started.\n")
    log.close()
    print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print "The Thread"+threading.current_thread().name+"Has Ended."