#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """Has public attribute area"""
    def area(self):
        """raise exception when called"""
        raise Exception("area() is not implemented")
