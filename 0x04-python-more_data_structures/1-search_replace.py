#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replace all occurences of 'search' with 'replace' in list"""
    new_list = []
    for x in my_list:
        if x is search:
            new_list.append(replace)
        else:
            new_list.append(x)
    return new_list
