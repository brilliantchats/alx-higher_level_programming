#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    """A basic calculator"""
    length = len(sys.argv)
    operators = ['+', '-', '*', '/']
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]
    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        print(sys.exit(1))
    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    main()
