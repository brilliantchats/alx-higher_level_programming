#!/usr/bin/python3
"""
returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    returns lists of ints of pascal's triangle up to n
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
            prev = [1, 1]
        else:
            temp = []
            temp.append(1)
            for j in range(1, i):
                temp.append(prev[j] + prev[j-1])
            temp.append(1)
            prev = temp
            triangle.append(temp)
    return triangle

