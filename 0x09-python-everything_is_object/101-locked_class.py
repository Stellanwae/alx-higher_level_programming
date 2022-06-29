#!/usr/bin/python3
class LockedClass:
    """Class that prevents the user from dynamically creating new instance
    except for attribute first_name"""
    __slots__ = ['first_name']
