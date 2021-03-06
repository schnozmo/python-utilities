#!/usr/bin/python

import re
import fileinput

def dec2bitarray(n):
    """return a list containing 1 bit for each"""
    result = []
    while n >0:
        result.insert(0, n & 1)
        n = n >> 1
    return result

def dec2hex(n):
    s = hex(n)
    s = s.replace("0x", "")
    if len(s) % 2:
        s = "0" + s

    return "0x" + s

def hex2dec(s):
    return int(s, 16)

for line in fileinput.input():
    line = line.rstrip('\r\n')
    input = int(line)
    print input, "-", dec2hex(input), "-", dec2bitarray(input)


