#!/usr/bin/python3
"""
This module define a square class that have as attributes size and position,
which get control over them through setters and getters. The class has
__init__() method that initializes instances and __str__() that invoked when
when printing objects/instances as alternative to using my_print() function,
in addition to area() and my_print() that calculate the area of a square and
prints its shape.
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
        Initializes a new instance of the Square class.

        Args:
            size(int): the size of the square.
            position(tuple): A tuple of 2 positive integers representing
                             the position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrives the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Seta the size of the square.

        Args:
            value(int): The size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError:if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an intger")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrives the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.

        Args:
            Value (tuple): A tuple of 2 positive integers representing
                            the position.

        Raises:
            TypeError: If position is not tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character '#'.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Function invoked inside print() function when trying to peint
        an object/instance and behave same as my_print() function.
        """
        if self.__size == 0:
            return ""
        result = []
        for _ in range(self.__position[1]):
            result.append("\n")
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size + "\n")
        return "".join(result).rstrip()
