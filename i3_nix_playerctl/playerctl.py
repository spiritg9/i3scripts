#!/usr/bin/env python
import os
import sys
import time



try:
    player = os.environ["BLOCK_INSTANCE"]
except:
    player = "audacious"
try:
    buttonValue = os.environ["BLOCK_BUTTON"]
except:
    buttonValue = ""

cmdTitle = "playerctl -p %s metadata title" % player 
cmdStatus = "playerctl -p %s status" % player 

title = os.popen(cmdTitle)
title = title.read().strip()

status = os.popen(cmdStatus)
status = status.read().strip()

if player == "audacious" and (title is None or title == "(null)" or title == ""):
    title = ""
    if buttonValue != '':
        if buttonValue == "1":
            o = os.popen("audacious")


maxLen = 30 
maxLen = maxLen - 3 # for player chars
l = len(title)
if l == 0:
    print(" ")
elif l > maxLen:
    i = int(time.time()%(l-maxLen))
    if i + maxLen >= l:
        i = l - maxLen 
    print(title[i:i+maxLen+1])
else:
    print(title)

if status == "Playing":
    print("#00AFFF")
    print("#00AFFF")
elif status == "Paused":
    print("#9616DB")
    print("#9616DB")
else:
    print("#FF0000")
    print("#FF0000")

if buttonValue != '':
    if buttonValue == "1":
        os.popen("playerctl -p %s play-pause" %player)
    elif buttonValue == "2" and player == "audacious":
        os.popen("killall audacious")
    elif buttonValue == "3":
        os.popen("playerctl -p %s stop" %player)
    elif buttonValue == "4":
        os.popen("playerctl -p %s volume 0.2+" %player)
    elif buttonValue == "5":
        os.popen("playerctl -p %s volume 0.2-" %player)
    elif buttonValue == "8":
        os.popen("playerctl -p %s next" %player)
    elif buttonValue == "9":
        os.popen("playerctl -p %s previous" %player)

