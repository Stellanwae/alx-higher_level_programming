#!/usr/bin/python3
"""
Defines class Rectangle
"""


class Rectangle:
    """ The rectangle"""
    def __init__(self, width = 0, height = 0):
        """Initialises Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance height"""
        return self.__height

    @height.setter:
    def height(self, value):
        """setter for private instance height"""
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
