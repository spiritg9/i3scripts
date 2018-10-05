#!/usr/bin/env python
import os
import sys

volume = os.popen("pamixer --get-volume")
volume = volume.read().strip()
mute = os.popen("pamixer --get-mute")
mute = mute.read().strip()

if mute == "true":
    muteColor = "#ff0000"
elif mute == "false":
    muteColor = "#00ff00"

if "BLOCK_BUTTON" in os.environ:
    buttonValue = os.environ["BLOCK_BUTTON"]
    if buttonValue == "1":
        o = os.popen("pamixer -t")
    elif buttonValue == "4":
        o = os.popen("pamixer -i 2")
    elif buttonValue == "5":
        o = os.popen("pamixer -d 2")

print(volume + "%")
print(muteColor)
print(muteColor)
