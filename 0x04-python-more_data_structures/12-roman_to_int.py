#!/usr/bin/python3
def roman_to_int(roman_string):
    """converts a Roman numeral to an integer"""
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) is not str or roman_string is None:
        return 0
    length = len(roman_string)
    total = 0
    i = 0
    while i < length:
        if roman_string[i] == 'I':
            if (i + 1) < length and roman_string[i + 1] == 'V':
                total += 4
                i = i + 2
            elif (i + 1) < length and roman_string[i + 1] == 'X':
                total += 9
                i = i + 2
            else:
                total += roman_num.get(roman_string[i])
                i = i + 1
        elif roman_string[i] == 'V':
            total += roman_num.get(roman_string[i])
            i = i + 1
        elif roman_string[i] == 'X':
            if (i + 1) < length and roman_string[i + 1] == 'L':
                total += 40
                i = i + 2
            elif (i + 1) < length and roman_string[i + 1] == 'C':
                total += 90
                i = i + 2
            else:
                total += roman_num.get(roman_string[i])
                i = i + 1
        elif roman_string[i] == 'C':
            if (i + 1) < length and roman_string[i + 1] == 'D':
                total += 400
                i = i + 2
            elif (i + 1) < length and roman_string[i + 1] == 'M':
                total += 900
                i = i + 2
            else:
                total += roman_num.get(roman_string[i])
                i = i + 1
        elif roman_string[i] == 'L':
            total += roman_num.get(roman_string[i])
            i = i + 1
        elif roman_string[i] == 'D':
            total += roman_num.get(roman_string[i])
            i = i + 1
        elif roman_string[i] == 'M':
            total += roman_num.get(roman_string[i])
            i = i + 1
    return total
