#!/usr/bin/python3
class Square:
    """Represents class square"""
    def __init__(self, size=0):
        """initialise data"""
        self.__size = size

    @property
    def size(self):
        """returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the cuurent square area"""
        return (self.__size ** 2)
