#!/usr/bin/python3

def print_last_digit(number):
    abnum = abs(number)
    last_num = int(10 * (abnum / 10 - int(abnum / 10)))
    print(last_num, end='')
    return last_num
