#!/usr/bin/env python
import os
import sys

def startIt(instance):
    startCommand = "doas openvpn --config /home/erni/.ovpn/%s.ovpn --writepid /home/erni/.ovpn/%s.pid --daemon --log /home/erni/.ovpn/%s.log" % (instance, instance, instance)
    os.system(startCommand)

def killIt(pid):
    os.system("doas kill -9 %s" % pid)

def printIt(text, color):
    print(text)
    print(color)
    print(color)

def isRunning(instance):
    filename = "/home/erni/.ovpn/%s.pid" % instance
    if os.path.isfile(filename):
        # get pid
        pid = os.popen("doas cat %s" % filename)
        pid = pid.read().strip()

        isRunning = os.popen("ps -p %s -o comm=" % pid)
        isRunning = isRunning.read().strip()

        if len(isRunning) > 0:
            return pid
    return "" 

if __name__ == "__main__":
   # get instance
    if not "BLOCK_INSTANCE" in os.environ:
        exit(0)
    instance = os.environ["BLOCK_INSTANCE"]

    pid = isRunning(instance)

    if pid != "":
        color = "#00ff00"
        text = "UP"
    else:
        color = "#ff0000"
        text = "DOWN"


    if "BLOCK_BUTTON" in os.environ:
        buttonValue = os.environ["BLOCK_BUTTON"]
        if buttonValue == "1" and pid == "":
            startIt(instance)
            if instance == "erniRL":
                os.system("doas cp /etc/resolv.conf /etc/resolv-beforeVPN.conf")
                os.system("doas cp /etc/resolv-rl.conf /etc/resolv.conf")
        elif buttonValue == "3" and pid != "":
            killIt(pid)
            if instance == "erniRL":
                os.system("doas cp /etc/resolv-beforeVPN.conf /etc/resolv.conf") # copy cloudflare dns on killing rl vpn

    printIt(text, color)

