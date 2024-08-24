#!/usr/bin/python3
"""
This module define a class square that calculate and compare the
area if squares.
"""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (float or int): The size of the square's sides.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int, optional): The size of the square's sides.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square's sides.

        Returns:
            float or int: The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square's sides.

        Args:
            value (float or int): The size of the square's sides.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares if the current square is equal to another square based
        on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares if the current square is not equal to another square based
        on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compares if the current square is less than another square based on
        their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square's area is less than the other
            square's area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares if the current square is less than or equal to another
        square based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square's area is less than or equal
            to the other square's area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compares if the current square is greater than another square based
        on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square's area is greater than the other
            square's area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares if the current square is greater than or equal to another
        square based on their areas.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the current square's area is greater than or equal
            to the other square's area, False otherwise.
        """
        return self.area() >= other.area()
