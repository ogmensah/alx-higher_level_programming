#!/usr/bin/python3
""" This module contains function which
checks an object is an instance of a class
or of a class that inherited form
"""


def is_kind_of_class(obj, a_class):
    """Define if a obj is instance of class"""
    if isinstance(obj, a_class):
        return True
    return False
