#! /usr/bin/env python3

import os
from requests import get
from json import loads as jloads

w = get("https://ipinfo.io")
ipinfo = jloads(w.text)
if "ip" not in ipinfo:
    print("error 001")
    print("#ff0000")
    print("#ff0000")
    exit(1)
elif "country" not in ipinfo:
    print("error 002")
    print("#ff0000")
    print("#ff0000")
    exit(1)

ip = ipinfo["ip"].strip()
country = ipinfo["country"].strip()

#print(ipinfo)
if ip == "45.32.233.31":
    print(ip)
    print("#00ff00")
    print("#00ff00")
elif country == "HR":
    print(ip)
    print("#ffff00")
    print("#ffff00")
else:
    print(ip)
    print("#ff0000")
    print("#ff0000")

# = os.environ["BLOCK_INSTANCE"]

