#!/usr/bin/python3
"""
This module define a square shape class that calculate its area,
also access and update its private attribute through getters and
setters which is here '__size'.
"""


class Square:
    """
    This is a class that represent a square shape.

    Attributes:
        __size: Private instance attribute of square's size.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the square class.

        Args:
            size: The size of the square.
        """

        self.__size = size

    @property
    def size(self):
        """
        Use property to get and set the value of private instance attribute
        __size using 'setters' and 'getters'.
        """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Method that return the area of a square.
        """
        return self.__size * self.__size
