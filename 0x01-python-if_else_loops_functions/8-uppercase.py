#!/usr/bin/python3
def uppercase(str):
    """Prints given string in uppercase"""
    length = len(str)
    if (length == 0):
        return ""
    for i in range(length):
        c = ord(str[i])
        if 97 <= c <= 122:
            c = c - 32
        if i != length - 1:
            print("{}".format(chr(c)), end="")
        else:
            print("{}".format(chr(c)))
