#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Adds element to copy of list"""
    l_len = len(my_list)
    if idx >= l_len or idx < 0:
        return (my_list)

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
