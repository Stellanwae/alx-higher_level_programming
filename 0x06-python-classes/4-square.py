#!/usr/bin/python3
"""Define class Square"""


class Square:
    """
    """
    def __init__(self, size=0):
        """
        """
        self.size = size

    def area(self):
        """
        """
        return int(self.__size) * int(self.__size)

    @property
    def size(self):
        """
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
