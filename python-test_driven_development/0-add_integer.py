#!/usr/bin/python3
def add_integer(a, b=98):
    # Check if both inputs are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert to integers if inputs are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Perform addition and return the result
    return int(a + b)
