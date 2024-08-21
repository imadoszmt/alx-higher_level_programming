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

    def __init__(self, size=0):
        """
        Initializes a new instance of the square class.

        Args:
            size: The size of the square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
