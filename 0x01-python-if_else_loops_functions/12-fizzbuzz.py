#!/usr/bin/python3
for i in range(1, 101):
    if i % 3 == 0:
        print("FIZZ", end=' ')
    if i % 5 == 0:
        print("BUZZ", end=' ')
    elif i % 3 != 0 and i % 5 != 0:
        print("{:d}".format(i), end=' ')
