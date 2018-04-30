#!/usr/bin/env python
import os
import sys

o = os.popen("amixer -D pulse sget Master | grep -F '['")
o = o.read()
indexV = o.index("%")
indexM = o.rindex("[")
# print o[indexV-2:indexV+1]
# print o[indexM+1:indexM+3]

if (sys.argv[1] == 'v'):
    if (o[indexV-2] == '0'):
        print(o[indexV-3:indexV])
    elif (o[indexV-2] == '['):
        print(o[indexV-1:indexV])
    else:
        print(o[indexV-2:indexV])
elif (sys.argv[1] == 'c'):
    if (o[indexM+1:indexM+3] == "on"):
        print("00FF00")
        print("00FF00")
    else:
        print("FF0000")
        print("FF0000")

#os.system('echo pero')
'''
if (o[7:9] == "us"):
  os.system('setxkbmap -layout "hr"')
else:
  os.system('setxkbmap -layout "us"')
'''
