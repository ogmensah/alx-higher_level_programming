#!/usr/bin/python3
# 8-rectangle.py
""" File name : 10-square.py
    It is not allowed to import any module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Spuare that inherits from class 'Rectangle'
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
        elf.__size = size
