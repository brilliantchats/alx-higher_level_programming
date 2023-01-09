#!/usr/bin/python3
def multiple_returns(sentence):
    """returns tuple length of a string and its first character"""
    length = len(sentence)
    if length == 0:
        return length, None
    return length, sentence[0]
