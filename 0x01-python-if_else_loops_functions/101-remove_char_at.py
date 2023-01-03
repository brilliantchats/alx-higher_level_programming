#!/usr/bin/python3
def remove_char_at(str, n):
    """Return a copy of str but removed the char at nth"""
    length = len(str)
    str_cpy = []
    for i in range(length):
        if (i != n):
            str_cpy.append(str[i])
    newstr = ''.join(str_cpy)
    return newstr
