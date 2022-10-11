#!/usr/bin/python3
class Square:
    """Represents a class square 
    and private instance attribute: size"""
    def __init__(self, size=0):
        """initialise data"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method: 
        
        Returns:
        int: current square area

        """
        return (self.__size ** 2)
