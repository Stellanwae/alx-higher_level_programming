#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        number = 0
        dem = 0
        for tups in my_list:
            number += (tups[0] * tups[1])
            dem += tups[1]
        return (number / dem)
    return 0
