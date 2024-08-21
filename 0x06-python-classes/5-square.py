#!/usr/bin/python3
"""
This module define a square shape class that have as attributes
a private instance __size, which we get control over it through
setters and getters. Ass a methods it have the initializer __init__
and area() and my_print which they calculate and print the area of
the square successively.
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

    def my_print(self):
        """
        Method that print the square based on the provided size.
        """
        printed_size = self.__size

        if printed_size == 0:
            print()

        line = 0
        while line < printed_size:
            printed_dash = 0
            while printed_dash < printed_size:
                print(f'#', end='')
                printed_dash += 1
            print()
            line += 1
