#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if type(a_dictionary) is not dict:
        return None
    if a_dictionary == {}:
        return None
    maximum = max(list(a_dictionary.values()))
    for k, v in a_dictionary.items():
        if v == maximum:
            return k
