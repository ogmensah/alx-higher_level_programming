#!/usr/bin/python3
# 1-number_of_lines.py
""" File name : 1-number_of_lines.py
    Using the with statement
    No module imported
"""


def number_of_lines(filename=""):
    """number_of_lines: returns the number of lines of a text file:
    Args:
        filename (str): content of the file. Defaults to "".
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return len(f.readlines())
