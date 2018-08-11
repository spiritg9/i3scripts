#! /bin/env python3

import xml.etree.ElementTree as ET
from requests import get

w = get("http://vrijeme.hr/hrvatska_n.xml")

POSTAJA = "Zagreb-Maksimir"
TEMP = "Temp"
VRIJEME = "Vrijeme"

# print(w.text)

e = ET.fromstring(w.text)
for child in e.findall('Grad'):
    grad = child.find('GradIme').text
    if grad == POSTAJA:
        podatci = child.find('Podatci')
        temp = podatci.find(TEMP).text.strip()
        vrijeme = podatci.find(VRIJEME).text.strip()
        if "kiša" in vrijeme:
            print("☔" + temp + "℃")
        elif "oblačno" in vrijeme:
            print("☁" + temp + "℃")
        elif "snijeg" in vrijeme or "susnježica" in vrijeme:
            print("❆" + temp + "℃")
        elif "grom" in vrijeme or "grmljavina" in vrijeme:
            print("ϟ" + temp + "℃")
        elif "sunčano" in vrijeme or "sunce" in vrijeme:
            print("☀" + temp + "℃")
        else:
            print("w" + temp + "℃")
        tempI = float(temp)
        if tempI < -10:
            print("#ffffff")
            print("#ffffff")
        elif tempI <= 0:
            print("#008fff")
            print("#008fff")
        elif tempI < 10:
            print("#00ffff")
            print("#00ffff")
        elif tempI < 20:
            print("#ffff00")
            print("#ffff00")
        elif tempI < 30:
            print("#ff8f00")
            print("#ff8f00")
        elif tempI > 30:
            print("#ff0000")
            print("#ff0000")
