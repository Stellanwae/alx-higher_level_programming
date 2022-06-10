#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if ord('a') <= ord(c) <= ord('z'):
            s = chr(ord(s) - (ord('a') - ord('A')))
            print("{:s}".format(s), end='')
        print("")
