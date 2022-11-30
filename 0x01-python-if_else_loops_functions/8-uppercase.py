#!/usr/bin/python3

def uppercase(str):
    for c in str:
        oc = ord(c)
        if oc >= 97 and oc <= 122:
            oc = oc - 32
        print("{:c}".format(oc), end='')
    print()
