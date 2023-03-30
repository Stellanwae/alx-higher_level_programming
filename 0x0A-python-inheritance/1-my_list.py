#!/usr/bin/python3
"""
MyList class
"""


class MyList(list):
    """child class of list"""
    def __init__(self):
        """inherits list object"""
        super().__init__()

    def print_sorted(self):
        """prints list"""
        print(sorted(self))
