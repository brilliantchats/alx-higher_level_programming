#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides elements from 2 lists elem by elem"""
    result_list = []
    for i in range(list_length):
        try:
            x, y = my_list_1[i], my_list_2[i]
            try:
                result_list.append(x / y)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except (ValueError, TypeError):
                print("wrong type")
                result_list.append(0)
        except IndexError:
            print("out of range")
            result_list.append(0)
    return result_list
