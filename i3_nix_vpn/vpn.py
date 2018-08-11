#!/usr/bin/env python
import os
import sys
from os.path import join

PID_PATH = "/home/erni/.ovpn/"
OPEN_VPN_CONF =
START_COMMAND = "openvpn --config /home/erni/.ovpn/erniLaptop.ovpn --writepid /home/erni/.ovpn/erniDO.pid"

if len(sys.argv) > 1:
    # PID file is should be called `instance`.pid
    instance = sys.argv[1]
else:
    print("error, missing arg")
    exit(1)

path = join(PID_PATH, instance)
path = "%s.pid" % path
print(path)
command = "ps -p $(cat %s) -o comm=" % path

if len(sys.argv) > 2:
    button = sys.argv[2]
    if button == "1":
        start_path = join(START_PATH, instance)
        #print("sudo %s_vpn.start > %s" %(start_path, path))
        process = os.popen(
            "sudo %s_vpn.start > /dev/null --write-pid %s" %
            (start_path, path))
    if button == "3":
        print("sudo kill -9 $(cat %s)" % path)
        process = os.popen("sudo kill -9 $(cat %s)" % path)
        f = open(path, "w+")
        f.write(" ")
        exit(0)

process = os.popen(command)
process = process.read()

if process is None or process == "":
    color = "#ff0000"
else:
    color = "#00ff00"

print("VPN")
print(color)
print(color)
