#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    for no in range:
        try:
            print("{:d}".format(my_list[no]), end='')
            no = no + 1
        except IndexError:
            break
    print()
    return no
