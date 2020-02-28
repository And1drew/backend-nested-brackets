#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "???"

import sys

openings = ["(*", "(", "[", "{", "<"]
closings = ["*)", ")", "]", "}", ">"]


def is_nested(line):
    """Validate a single input line for correct nesting"""
    stack = []
    token_counter = 0
    while line:
        token = line[0]
        if line.startswith("(*"):
            token = "(*"
        elif line.startswith("*)"):
            token = "*)"

        token_counter += 1
        line = line[len(token):]

        if token in openings:
            stack.append(token)
        elif token in closings:
            closer_index = closings.index(token)
            expected_opener = openings[closer_index]
            if stack.pop() != expected_opener:
                return "No " + str(token_counter)

    if stack:
        return "No " + str(token_counter)
    return "Yes"


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    print("testing for nesting: {}".format(args[0]))
    with open(args[0]) as ifile:
        with open('output.txt', 'w') as ofile:
            for line in ifile:
                result_str = is_nested(line)
                print(result_str)
                ofile.write(result_str + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])

# the demo walkthrough was very helpful in solving this kata