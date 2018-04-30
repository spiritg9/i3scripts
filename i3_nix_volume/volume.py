#!/usr/bin/env python
import os
import sys
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.info("test")

volume = os.popen("pamixer --get-volume")
volume = volume.read().strip()
mute = os.popen("pamixer --get-mute")
mute = mute.read().strip()

if mute == "true":
    muteColor = "#ff0000"
elif mute == "false":
    muteColor = "#00ff00"

if len(sys.argv) > 1:
    buttonValue = sys.argv[1]
    if buttonValue != '':
        if buttonValue == "1":
            o = os.popen("pamixer -t")
        elif buttonValue == "4":
            o = os.popen("pamixer -i 2")
        elif buttonValue == "5":
            o = os.popen("pamixer -d 2")

print(volume + "%")
print(muteColor)
print(muteColor)
