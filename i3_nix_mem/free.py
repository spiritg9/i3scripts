#!/usr/bin/env python3
import os
import sys

# print o[indexV-2:indexV+1]
# print o[indexM+1:indexM+3]

o = os.popen("free | grep Mem | awk '{ print $7 }' ")
o = o.read().strip()

free =  float(o)
free =  free / 1000000
print("%.2fG" %free)
if free < 1.:
    print("#ff0000")
    print("#ff0000")
elif free < 2.:
    print("#ff8f00")
    print("#ff8f00")
elif free < 3.:
    print("#ffff00")
    print("#ffff00")
elif free < 6.:
    print("#00ff00")
    print("#00ff00")
else:
    print("#00ffff")
    print("#00ffff")
