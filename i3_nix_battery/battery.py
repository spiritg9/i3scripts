#!/usr/bin/env python3
import os

def get_color(percentage):
    percent = int(percentage[:-1])
    
    if percent < 10:
        # exit code 33 will turn background red
        return "#FF0000"
    if percent < 20:
        return "#FF0000"
    if percent < 30:
        return "#EE5C42"
    if percent < 40:
        return "#FFA500"
    if percent < 50:
        return "#FFCC00"
    if percent < 60:
        return "#F0FF00"
    if percent < 70:
        return "#FFFF00"
    if percent < 80:
        return "#00FF00"
    return "#00AFFF"

def print_color(color):
    print(color)
    print(color)

def main():
    command = os.popen("upower -i /org/freedesktop/UPower/devices/battery_BAT0")
    command_output = command.read().strip()

    lines = command_output.split("\n")

    state = "unknown"
    percentage = 0
    time_to_empty = 0
    time_to_full = 0


    for line in lines:
        line = line.strip()
        if line.startswith("state"):
            if "discharging" in line:
                state = "discharging"
            elif "charging" in line:
                state = "charging"
            elif "fully-charged" in line:
                state = "full"
        elif line.startswith("time to full"):
            x = line.find(":")
            time_to_full = line[x+1:].strip()
        elif line.startswith("time to empty"):
            x = line.find(":")
            time_to_empty = line[x+1:].strip()
        elif line.startswith("percentage"):
            x = line.find(":")
            percentage = line[x+1:].strip()

    short_state = "?"
    time = ""
    if state == "charging":
        short_state = "+"
        time = "({time})".format(time=time_to_full)
    elif state == "discharging":
        short_state = "-"
        time = "({time})".format(time=time_to_empty)
    elif state == "full":
        short_state = ""
        time = ""

    output_string = short_state + percentage + " " + time
    color = get_color(percentage)

    print(output_string)
    print_color(color)

if __name__ == "__main__":
    main()
    

