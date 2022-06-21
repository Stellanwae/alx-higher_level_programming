#!/usr/bin/python3
def safe_print_integer(value):
    for i in value:
        try:
            print("{:d}".format(value), end="")
        except TypeError:
            return False
