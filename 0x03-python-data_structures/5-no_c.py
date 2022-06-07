#!/usr/bin/python3
def no_c(my_string):
    for m in my_string:
        if m != 'c' and m != 'C':
            print('{:c}'.format(my_string))
