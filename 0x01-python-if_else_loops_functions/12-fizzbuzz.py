#!/usr/bin/python3
for i in range(1, 101):
    if i % 3 == 0:
        print("FIZZ", end=' ')
    if i % 5 == 0:
        print("BUZZ", end=' ')
    if i % 3 == 0and i % 5 == 0:
        print("{:d}".format(i), end=' ')
    else:
        print(i, end=' ')
