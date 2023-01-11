#!/usr/bin/python3
"""The is module of base geometry class"""


class BaseGeometry(object):
    """Defines class base geometry"""
    def area(self):
        """computes area
        Raises:
            Exeptions: [area() is not implemented]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer values
        Arguments:
            name {str} -- name of an instance
            value {int} -- type of instance
        Raises:
            TypeError: [must be an integer]
            ValueError: [must be greater than 0]
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
