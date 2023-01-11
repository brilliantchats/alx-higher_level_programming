#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """ deletes a key in a dictionary"""
    a_dictionary.pop(key, 0)
    return a_dictionary
