#!/usr/bin/python3
""" This module contains fxn which checks an obj is instance of a cls"""


def is_same_class(obj, a_class):
    """Define if a obj is instance of class"""
    if type(obj) == a_class:
        return True
    return False
