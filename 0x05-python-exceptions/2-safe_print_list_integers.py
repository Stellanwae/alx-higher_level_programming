#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    for int(i) in my_list:
        try:
            print("{:d}".format(i), end="")
        except IndexError:
            print("List out of range")
    print("{:d}".format, (end="\n")

            
