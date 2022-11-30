#!/usr/bin/python3

for i in range(-122, -96):
    i = -i
    if i % 2 == 1:
        i -= 32
    print("{:c}".format(i), end='')
