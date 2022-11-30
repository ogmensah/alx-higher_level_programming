#!/usr/bin/python3

def remove_char_at(str, n):
    st = ""
    for a, c in enumerate(str):
        if a != n:
            st = st + c
    return st
