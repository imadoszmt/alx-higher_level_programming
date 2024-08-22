#!/usr/bin/python3
"""
This module define a square shape class that have as attributes
a private instances __size and __position, which get control over
them through setters and getters. The class has __init__() method
that initializes instances, in addition to area() and my_print()
that calulate the area of a square and print its shape.
"""


class Square:
    """
    This is a class that represent a square shape.

    Attributes:
        __size: Private instance attribute of square's size.
        __position: Private instance attribute of position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Method that initializes a new instance of the square class.

        Args:
            size (int): The size of the square.
            position (tuple): A tuple (x, y), where x is the number of spaces
                    before each line of square and y is the number of
                    empty line to print before the square starts.
    """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Use property to get and set the value of private instance attribute
        __size using 'setters' and 'getters'.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Use property to get and set the value of the private instance
        attribute __position using 'getters' and 'setters'.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or 
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Method that return the area of a square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Method that print the square based on the provided size. In addition
        use the value of position tuple(x, y) to set the number of line before
        start printing the lines of the square with y value and the reserved
        space beforehand each square line with x value.
        """

        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
