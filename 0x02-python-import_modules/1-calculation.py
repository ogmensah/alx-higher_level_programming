#!/usr/bin/python3
from calculator_1 import add, mul, div, sub
a = 10
b = 5
print(f"{} + {} = {}".format(a, b, add(a, b)))
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
