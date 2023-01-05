#!/usr/bin/python3
import hidden_4


def main():
    """Print the names defined in the imported module"""
    names = dir(hidden_4)
    for string in names:
        if string[:2] != "__":
            print("{}".format(string))


if __name__ == "__main__":
    main()
