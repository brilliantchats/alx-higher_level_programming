#!/usr/bin/python3
def islower(c):
    """Checks whether c is lowercase or not"""
    num_of_char = ord(c)
    if 97 <= num_of_char <= 122:
        return True
    else:
        return False
