#!/usr/bin/python3

a = 1
b = 2

if __name__ == "__main__":
    result = __import__('add_0').add(a, b)
    print("{} + {} = {}".format(a, b, result))
