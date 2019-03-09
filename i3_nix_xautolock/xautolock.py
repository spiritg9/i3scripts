#!/usr/bin/env python
import os
import sys

AUTO_LOCK_TIME = 5

def startIt():
    startCommand = 'DISPLAY=:0.0 nohup xautolock -time %s -locker "~/.i3/lock" > /dev/null &' %AUTO_LOCK_TIME
    os.system(startCommand)

def killIt(pid):
    os.system("doas kill -9 %s" % pid)

def printIt(text, color):
    print(text)
    print(color)
    print(color)

def isRunning():
    isRunning = os.popen("pgrep xautolock")
    pid = isRunning.read().strip()

    if len(pid) > 0:
        return pid
    return "" 

def getColorText(pid):
    if pid != "":
        color = "#00ff00"
        text = "AUTOLOCK"
    else:
        color = "#ff0000"
        text = "OFFLOCK"
    return color, text

def isVideoPlaying():
    # add here to check if something is full screen
    isRunning = os.popen("playerctl -a status")
    statuses = isRunning.read().split("\n")
    for status in statuses:
        if status == "Playing":
            return True
    return False

if __name__ == "__main__":
    pid = isRunning()
    color, text = getColorText(pid)


    if "BLOCK_BUTTON" in os.environ:
        buttonValue = os.environ["BLOCK_BUTTON"]
        if buttonValue == "1" and pid == "":
            startIt()
            pid = isRunning()
            color, text = getColorText(pid)
        elif buttonValue == "3" and pid != "":
            killIt(pid)
            pid = isRunning()
            color, text = getColorText(pid)

    printIt(text, color)

