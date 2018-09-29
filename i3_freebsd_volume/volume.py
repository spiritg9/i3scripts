#!/usr/bin/env python3
import os
import sys

def print_volume(volume, muteColor):
    print(volume + "%")
    print(muteColor)
    print(muteColor)

volume = os.popen("aumix -q | grep vol")
volume = volume.read().split(" ")[2].strip()
#mute = os.popen("pamixer --get-mute")
#mute = mute.read().strip()


if volume == "0":
    mute = True;
    muteColor = "#ff0000"
else:
    mute = False;
    muteColor = "#00ff00"

try:
    buttonValue = os.environ["BLOCK_BUTTON"]
except:
    buttonValue = ''

if buttonValue != '':
    if buttonValue == "1":
        if mute: 
            o = os.popen("aumix -L")
            print_volume(volume, muteColor)
        else:
            o = os.popen("aumix -S")
            o = os.popen("aumix -v 0")
            print_volume(volume, muteColor)
    elif buttonValue == "4":
        o = os.popen("aumix -v +5%")
        o = os.popen("aumix -S")
        print_volume(volume, muteColor)
    elif buttonValue == "5":
        o = os.popen("aumix -v -5%")
        o = os.popen("aumix -S")
        print_volume(volume, muteColor)
else:
    print_volume(volume, muteColor)

