#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    addition = 0
    for arg in sys.argv[1:]:
        addition += int(arg)
    print("{:d}".format(addition))
