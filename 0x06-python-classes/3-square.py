#!/usr/bin/python3
"""
This module define a square shape class
"""


class Square:
    """
    This is a class that represent a square shape.

    Attributes:
        __size: Private instance attribute of square's size.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the square class.

        Args:
            size: The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Method that return the area of a square
        """
        return self. __size * self.__size
