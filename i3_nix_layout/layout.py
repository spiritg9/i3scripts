#!/usr/bin/env python3
import os
import sys

# print o[indexV-2:indexV+1]
# print o[indexM+1:indexM+3]

o = os.popen("setxkbmap -query | grep layout | cut -d: -f2- | sed 's/ //g'")
o = o.read().strip()
print(o)

if o == 'us':
    print("#00ff00")
    print("#00ff00")
elif o == 'hr':
    print("#ff0000")
    print("#ff0000")
