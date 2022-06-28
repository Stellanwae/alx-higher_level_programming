#!/usr/bin/python3
"""
Defines the class Rectangle
"""


class Rectangle:
    """Represents the rectangle"""
    def __init__(self, width = 0, height = 0):
        """initialise width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """To return self"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter that defines the private attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """to return self"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0)

    def area(self):
        """Public instance, want rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance to return perimeter
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2(self.__width + self.__height))

    

