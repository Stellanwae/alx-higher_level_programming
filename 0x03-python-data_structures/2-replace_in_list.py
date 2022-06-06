#!/usr/bin/python3
def replace _in_list(my_list, idx, element):
        if idx < o or idx >= len(my_list):
                return my_list
        my_list[idx] = element
        return my_list
