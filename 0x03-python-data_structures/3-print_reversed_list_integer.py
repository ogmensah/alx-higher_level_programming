#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """prints integers in the list in the reverse order"""
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
