#!/usr/bin/python3
class Square:
    """Square class with private instance attribute: size"""
    def __init__(self, size=0):
        """initialise data"""
        self.__size = size

    @property
    def size(self):
        """retrieve size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current area"""
        return (self.__size ** 2)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
