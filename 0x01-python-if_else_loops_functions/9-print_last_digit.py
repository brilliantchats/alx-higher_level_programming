#!/usr/bin/python3
def print_last_digit(number):
    """Prints the last digit of the given number"""
    if number < 0:
        last_digit = (number * -1) % 10
    else:
        last_digit = number % 10
    print("{}".format(last_digit), end="")
    return last_digit
