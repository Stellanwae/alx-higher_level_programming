#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            s = chr(ord(s) - 32)
        else:
            s = chr(ord(s))
        print("{:s}".format(s), end='')
        print("", end='')
           
