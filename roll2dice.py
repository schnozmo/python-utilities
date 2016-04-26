#!/usr/bin/python

import random
import sys

def roll_dice():
    return random.randint(1,6)

ind_count = {}
tot_count = {}
tot_rolls = 0

max_rolls = 0
if len(sys.argv) > 1:
    if sys.argv[1].isdigit():
        max_rolls = int( sys.argv[1] )
    
keep_going = 1
while keep_going == 1:
    tot_rolls+=1
    d1 = roll_dice()
    d2 = roll_dice()
    total = d1 + d2

    if d1 in ind_count:
        ind_count[d1] += 1
    else:
        ind_count[d1] = 1

    if d2 in ind_count:
        ind_count[d2] += 1
    else:
        ind_count[d2] = 1
    
    if total in tot_count:
        tot_count[total] += 1
    else:
        tot_count[total] = 1
    

    print("Result is: %d + %d = %d" % (d1, d2, total))

    if max_rolls == 0:
        print "Another (Y)?"
        input = raw_input()
        if input.upper() != "Y":
            keep_going = 0

    elif tot_rolls >= max_rolls:
        keep_going = 0


print("Final result after %d rolls:" % tot_rolls)

print("\nSingle die frequency:")

for i in range(1,7):
    if i not in ind_count:
        ind_count[i] = 0
    
    frac = float( 100 * ind_count[i] )/( tot_rolls * 2)
    print("  Die %(die)d rolled %(n)d times (%(frac).2f%%)" % \
          {"die": i, "n": ind_count[i], "frac": float(frac)})

print("\nSingle die frequency:")

for i in range(2,12):
    if i not in tot_count:
        tot_count[i] = 0
    
    frac = float( 100 * tot_count[i] )/ tot_rolls
    print("  Sum %(total)d rolled %(n)d times (%(frac).2f%%)" % \
          {"total": i, "n": tot_count[i], "frac": float(frac)})
