#!/usr/bin/python3
"""
Module has the function is_same_class
"""


def is_same_class(a, a_class):
    """true if object is in same class as a_class returns false when otherwise"""
    return(type(a) == a_class)
