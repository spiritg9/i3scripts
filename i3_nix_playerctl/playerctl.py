#!/usr/bin/env python
import os
import sys
import time

MAXLEN = 30

def getTitle(player):
    cmdTitle = "playerctl -p %s metadata title" % player # prepare command
    title = os.popen(cmdTitle)                           # execute it
    return title.read().strip()                          # read the output and strip it 

def getStatus(player):
    cmdStatus = "playerctl -p %s status" % player        # prepaer command
    status = os.popen(cmdStatus)                         # execute it
    return status.read().strip()                         # read the output and strip it 

def getVolume(player):
    cmdVolume = "playerctl volume -p %s" % player        # prepaer command
    volume = os.popen(cmdVolume)                         # execute it
    volume = volume.read().strip()                       # read the output and strip it 
    volume = int(float(volume) * 100)                    # we don't want decimal number
    return str(volume) # we can't concatenate string with float, so return string

def printSongTitle(title, volume=None):
    maxLen = MAXLEN - 3 # for player chars

    l = len(title)
    if volume is not None:
        l = l + 3
    if l == 0:
        print(" ")
    elif l > maxLen:
        i = int(time.time()%(l-maxLen))
        if i + maxLen >= l:
            i = l - maxLen 
        if volume is not None:
            print(title[i:i+maxLen+1-3] + " " +volume)
        else:
            print(title[i:i+maxLen+1])
    else:
        if volume is not None:
            print(title)
        else:
            print(title + " " + volume)
    

def printColor(status):
    if status == "Playing":
        print("#00AFFF")
        print("#00AFFF")
    elif status == "Paused":
        print("#9616DB")
        print("#9616DB")
    else:
        print("#FF0000")
        print("#FF0000")

def defaultPrint(title, player):
    printSongTitle(title)
    # wait for player to register status 
    # change so it doesn't look laggy in bar
    # or else it will wait next second to
    # change color
    time.sleep(0.05) 
    print(getStatus(player))
    printColor(getStatus(player))
    

try:
    player = os.environ["BLOCK_INSTANCE"]
except:
    player = "audacious"
try:
    buttonValue = os.environ["BLOCK_BUTTON"]
except:
    buttonValue = ""

status = getStatus(player)
title = getTitle(player)

if player == "audacious" and (title is None or title == "(null)" or title == ""):
    title = ""
    if buttonValue != '':
        if buttonValue == "1":
            o = os.popen("audacious")


if buttonValue != '':
    if buttonValue == "1":
        os.popen("playerctl -p %s play-pause" %player)
        defaultPrint(title, player)
    elif buttonValue == "2" and player == "audacious":
        os.popen("killall audacious")
        defaultPrint(title, player)
    elif buttonValue == "3":
        os.popen("playerctl -p %s stop" %player)
        defaultPrint(title, player)
    elif buttonValue == "4":
        os.popen("playerctl -p %s volume 0.05+" %player) # if step is higher, it won't go near 100%
        printSongTitle(title, getVolume(player))
        printColor(status)
    elif buttonValue == "5":
        os.popen("playerctl -p %s volume 0.05-" %player) # if step is higher, it won't go near 100%
        printSongTitle(title, getVolume(player))
        printColor(status)
    elif buttonValue == "8":
        os.popen("playerctl -p %s next" %player)
        defaultPrint(title, player)
    elif buttonValue == "9":
        os.popen("playerctl -p %s previous" %player)
        defaultPrint(title, player)
else:
    defaultPrint(title, player)

