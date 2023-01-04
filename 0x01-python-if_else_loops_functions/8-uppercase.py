#!/usr/bin/python3
def uppercase(str):
    """Prints given string in uppercase"""
    length = len(str)
    str_list = []
    if length:
        for i in range(length):
            c = ord(str[i])
            if 97 <= c <= 122:
                str_list.append(chr(c - 32))
            else:
                str_list.append(chr(c))
        print("{}".format(''.join(str_list)))
    else:
        print("{}".format(''))
