#!/usr/bin/env python3
import os
import sys

# print o[indexV-2:indexV+1]
# print o[indexM+1:indexM+3]

o = os.popen("df -h | grep home | awk '{ print $4 }' ")
o = o.read().strip()

free =  float(o[:-1])
print("%sG" %free)
if free < 10:
    print("#ff0000")
    print("#ff0000")
elif free < 30:
    print("#ff8f00")
    print("#ff8f00")
elif free < 50:
    print("#ffff00")
    print("#ffff00")
elif free < 100:
    print("#00ff00")
    print("#00ff00")
else:
    print("#00ffff")
    print("#00ffff")
