#!/usr/bin/python3
def main():
    from add_0 import add

    a = 1
    b = 2

    print("{0:d} + {1:d} = {2:d}".format(a, b, add(1, 2)))

if __name__ == "__main__":
    main()
