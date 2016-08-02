#!/usr/bin/python

import random, time, sys

t = time.gmtime()
a = list(time.strftime("%H%M%S", t))
a.reverse()
b = time.strftime("%s", t)
astr = a[1] + a[3] + a[0] + a[2] + a[4] + a[5]
seed = int(b)%int(astr)

random.seed(seed)

lines = []
for l in sys.stdin:
	lines.append(l.rstrip("\r\n"))

while len(lines) > 0:
	i = random.randint(0, len(lines) - 1)
	print lines.pop(i)


