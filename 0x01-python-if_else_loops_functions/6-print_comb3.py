#!/usr/bin/python3
for j in range(0, 10):
    for k in range(0, 10):
        if ((j != k and j < k) and (j + k != 17)):
            print("{:d}{:d}, ".format(j, k), end='')
        elif (j == 8 and k == 9):
            print("{:d}{:d}".format(j, k))
