#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ != "__main__":
    exit()

if len(sys.argv) != 4:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    exit(1)

op = sys.argv[2]
n1 = int(sys.argv[1])
n2 = int(sys.argv[3])
if op not in ['+','-','*','/']:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

if op == '+':
    print(f"{n1} + {n2} = {add(n1, n2)}")
elif op == '-':
    print(f"{n1} - {n2} = {sub(n1, n2)}")
elif op == '*':
    print(f"{n1} * {n2} = {mul(n1, n2)}")
else:
    print(f"{n1} / {n2} = {div(n1, n2)}")

