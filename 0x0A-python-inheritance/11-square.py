#!/usr/bin/python3
# 8-rectangle.py
""" File name : 10-square.py
    It is not allowed to import any module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Spuare that inherits from multiple classes'
    Attributes:
    ----------
    size  {int} -- [square's size]
    """

    def __init__(self, size):
        """
        private attributes width and height,
        and validating if they are ints.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """print string"""
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
