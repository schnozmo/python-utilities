#!/usr/local/bin/python

import fileinput
import sys

n_line = 1
split_char = "|"

if len(sys.argv) == 2:
    split_char = sys.argv[1]


for line in sys.stdin:
    line = line.rstrip('\r\n')
    line_list = line.split(split_char)
    for field_no in range(len(line_list)):
        nice_field_no = field_no + 1
        print "Line %(line_no)d: Field %(nice_field_no)d: %(string)s" % \
          {"line_no": n_line, "nice_field_no": nice_field_no, "string": line_list[field_no]}
    n_line = n_line+1
