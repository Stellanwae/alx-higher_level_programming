#!/usr/bin/python3
def safe_print_division(a, b):
    c = a / b
    try:
        print("{:d} / {:d} = {:d}".format(a, b, c))
    else:
        return None
    finally:
        return c
