#!/usr/bin/python3
def uppercase(str):
    str1 = ''
    for s in str:
        if ord('a') <= ord(s) <= ord('z'):
            str1 = str1 + chr((ord(s) - 32))
        else:
            str1 = str1 + chr(ord(s))
        print("{:c}".format(str1))
