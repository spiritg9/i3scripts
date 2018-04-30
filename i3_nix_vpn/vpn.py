#!/usr/bin/env python
import os
import sys
import logging
from os.path import join

PID_PATH = "/home/erni/.ovpn/"

if len(sys.argv) > 1:
    pid_file = sys.argv[1]
else:
    print("error, missing arg")
    exit(1)

path = join(PID_PATH, pid_file)
command = "ps -p $(cat %s) -o comm=" % path

if len(sys.argv) > 2:
    button = sys.argv[2]
    if button == "1":
        process = os.popen("sudo ~/.myScripts/ovpnStart_vultr > ~/ovpn.log")
    if button == "3":
        process = os.popen("sudo kill -9 $(cat %s)" %path)
        f = open(path, "rw")
        f.write(" ")
        exit(0)

process = os.popen(command)
process = process.read()

if process == None or process == "":
    color = "#ff0000"
else:
    color = "#00ff00"

print("VPN")
print(color)
print(color)
