#!/usr/bin/python3
def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if a_dictionary == None:
        return None
    maximum = max(list(a_dictionary.values()))
    for k, v in a_dictionary.items():
        if v == maximum:
            return k
