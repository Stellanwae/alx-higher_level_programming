#!/usr/bin/python3
def print_reversed_list(my_list=[]):
    if my_list:
        for m in reversed(my_list):
            print('{:d}'.format(m), end='')
