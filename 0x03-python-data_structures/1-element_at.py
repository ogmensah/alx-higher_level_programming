#!/usr/bin/python3
def element_at(my_list, idx):
    """Returns an element at a given index in a list"""
    if idx < 0 or idx > len(my_list):
        return None
    return my_list[idx]
