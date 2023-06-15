#!/usr/bin/python3

def add_integers(a, b=98):
    '''
    Adds two integers.

    Args:
        a (int or float) The first number.
        b (int or float) The second number. defaults to 98.

    Returns:
        int: The sum of a and b, casted to a integer.

    Raises:
        TypeError: If a or b is not a integer or float.
     '''

    if type(a) not in [int, float]:
        raise TypeError('a must be an integer or b must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('a must be an integer or b must be an integer')

    a = int(a)
    b = int(b)
