#!/usr/bin/python3
"""
Prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """Print full name"""
    if type(first_name) != str or first_name == "":
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    """prints first_name last_name"""
    print("My name is {} {}".format(first_name, last_name))
