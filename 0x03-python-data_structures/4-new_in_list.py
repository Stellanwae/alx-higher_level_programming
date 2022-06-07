#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nl = my_list[:]
    if 0 > idx >= len(nl):
        nl[idx] = element
        return nl
    return my_list
