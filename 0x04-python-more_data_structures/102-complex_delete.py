#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary"""
    values = a_dictionary.values()
    if value in values:
        length = 0
        for v in values:
            if v == value:
                length += 1
        new_list = []
        for k, v in a_dictionary.items():
            if v == value:
                new_list.append(k)
        for i in range(length):
            del a_dictionary[new_list[i]]
    return a_dictionary
