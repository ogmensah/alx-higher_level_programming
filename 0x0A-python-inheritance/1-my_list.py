#!/usr/bin/python3
"""Module contains two classes of which one inherits from the other"""


class MyList(list):
    """List
    The lookup function searches and displays attributes of objects.
    Attributes:
        obj: input object."""

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))
