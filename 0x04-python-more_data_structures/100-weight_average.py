#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    if my_list == {}:
        return 0
    prod_total = 0
    average = 0
    for tupl in my_list:
        prod_total += (tupl[0] * tupl[1])
        average += tupl[1]
    return prod_total / average
