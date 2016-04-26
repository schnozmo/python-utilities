#!/usr/bin/python

import fileinput

def frametext(s):
     """This function takes a string and frames it with a star border
     
     the re is 1 line of vertical space and 2 characters of horizontal
     space around the string.
     """

     sl = len(s)
     allstarline = "*" * ( sl + 6 )
     endstarline = "*" + " " * (sl + 4) + "*"
     print allstarline
     print endstarline
     print "*  " + s + "  *"
     print endstarline
     print allstarline

for line in fileinput.input():
    line = line.rstrip('\r\n')
    frametext(line)

    
