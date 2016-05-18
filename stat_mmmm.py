#!/usr/bin/python

import sys, math

# mean, q1, median, q3, min, max, mode, stdev
val_count = {}
line_count = 0
sum_count = 0

for line in sys.stdin:
    line = float(line.rstrip('\r\n'))

    line_count += 1
    sum_count += line

    if line in val_count.keys():
        val_count[line] += 1
    else:
        val_count[line] = 1

mean = float(sum_count) / line_count

sum_sq = float(0)
all_vals = []
sorted_vals = sorted(val_count)
for v in sorted_vals:
    num_this_val = val_count[v]
    while num_this_val > 0:
        sum_sq += (v - mean) ** 2
        all_vals.append(v)
        num_this_val -= 1

median = all_vals[int(line_count/2)]
if line_count % 2 == 0:
    val1 = all_vals[int(line_count/2)]
    val2 = all_vals[int((line_count - 2)/2)]
    median = float(val1 + val2)/2

q1 = all_vals[int(line_count/4)-1]
q3 = all_vals[3 * int(line_count/4) - 1]
minimum = all_vals[0]
maximum = all_vals[line_count-1]
variance = sum_sq / (line_count - 1)
stdev = math.sqrt(variance)
print(" nline = %d\n   sum = %.4f\n  mean = %.4f\n    q1 = %.4f\nmedian = %.4f\n    q3 = %.4f\n   min = %.4f\n   max = %.4f\n   var = %.4f\n stdev = %.4f" % (line_count, sum_count, mean, q1, median, q3, minimum, maximum, variance, stdev))
