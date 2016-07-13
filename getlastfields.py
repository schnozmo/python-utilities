#!/usr/bin/python

import sys

n_fields = 1
split_char = "|"

if len(sys.argv) == 3:
    split_char = sys.argv[1]
    n_fields = sys.argv[2]

for line in sys.stdin:
    line = line.rstrip('\r\n')
    line_list = line.split(split_char)
    outline_list = []
    
    fields_left_to_pop = int(n_fields)
    while fields_left_to_pop > 0:
        outline_list.insert(0, line_list.pop())
        fields_left_to_pop -= 1

    outline = split_char.join(outline_list)
    print outline
