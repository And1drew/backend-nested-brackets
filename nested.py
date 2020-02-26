#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "???"

import sys


def is_nested(lines):
    """Validate a single input line for correct nesting"""
    results = [] 
    line_list = lines.split('\n')
    for line in line_list:
        paren_counter = 0
        bracket_counter = 0
        brace_counter = 0
        tag_counter = 0
        special_counter = 0
        for char, nextchar, specialchar in zip(line, line[1:], line[2:]):
            print(char, nextchar)

            if char == '(' and nextchar == '*' and specialchar == ')':
                print(char, nextchar, specialchar)
                print("hmm this is special indeed")
                special_counter += 1
                paren_counter -= 1

            elif char == '(' and nextchar == '*':
                special_counter += 1
            elif char == '*' and nextchar == ')':
                special_counter -= 1

            elif char == '(':
                paren_counter += 1
            elif char == ')':
                paren_counter -= 1

            elif char == '[':
                bracket_counter += 1
            elif char == ']':
                bracket_counter -= 1

            elif char == '{':
                brace_counter += 1
            elif char == '}':
                brace_counter -= 1

            elif char == '<':
                tag_counter -= 1
            elif char == '>':
                tag_counter -= 1

            elif special_counter < 0:
                results.append("No " + str(line.index(char)))
            elif tag_counter < 0:
                results.append("No " + str(line.index(char)))
            elif paren_counter < 0:
                results.append("No " + str(line.index(char)))
            elif brace_counter < 0:
                results.append("No " + str(line.index(char)))
            elif bracket_counter < 0:
                results.append("No " + str(line.index(char)))
    else:
        results.append("Yes")
    print(results)
    pass


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        text = f.read()
        result_list = is_nested(text)
        print(result_list)
    # Results: print to console and also write to output file
    pass


if __name__ == '__main__':
    main(sys.argv[1:])
