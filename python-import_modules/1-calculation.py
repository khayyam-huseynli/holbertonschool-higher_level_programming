#!/usr/bin/python3

from 1-calculation.py import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    result1 = add(a, b)
    print("{} + {} = {}".format(a, b, result1))

    result2 = sub(a, b)
    print("{} - {} = {}".format(a, b, result2))

    result3 = mul(a, b)
    print("{} * {} = {}".format(a, b, result3))

    result = div(a, b)
    print("{} / {} = {}".format(a, b, result4))
