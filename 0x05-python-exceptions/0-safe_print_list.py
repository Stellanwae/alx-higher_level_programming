#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    no = 0
    for y in range:
        try:
            print("{:d}".format(my_list[y]), end='')
            no = no + 1
        except IndexError:
            break
    print()
    return no
