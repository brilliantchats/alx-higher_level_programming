#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if (i + j) < 10 and i != 8:
            print("{}{}".format(i, i + j), end=", ")
        elif i == 8 and (i + j) < 10:
            print("{}{}".format(i, i + j))
