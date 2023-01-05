#!/usr/bin/python3
import sys


def main():
    """Add all command line args supplied"""
    length = len(sys.argv)
    total = 0

    if length == 1:
        print("{}".format(total))
    else:
        for i in range(1, length):
            total += int(sys.argv[i])
        print("{}".format(total))


if __name__ == "__main__":
    main()
