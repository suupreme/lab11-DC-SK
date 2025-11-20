# https://github.com/suupreme/lab11-DC-SK
# Partner 1: Daniel Cheng
# Partner 2: Sean Kwon

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math


def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except TypeError:
        raise ValueError


def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise ValueError


def add(a, b): 
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b) / math.log(a)


def exp(a, b):
    return a ** b
