#!/usr/bin/python3
"""Module contains function for printing attributes of class objects"""

def lookup(obj):
    """lookup
    The lookup function searches and displays attributes of objects.
    Attributes:
        obj: input object.
    """
    return dir(obj)
