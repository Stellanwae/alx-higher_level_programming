#!/usr/bin/python3
"""
Class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of square"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Area of the square"""
        return self.__size ** 2
