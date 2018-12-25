# -*- coding: utf-8 -*-

def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False

_input = int(input("Jahreszahl eingeben: "))
print()
if isLeapYear(_input):
    output = "ist ein Schaltjahr"
else:
    output = "ist kein Schaltjahr"
print(_input, output)
