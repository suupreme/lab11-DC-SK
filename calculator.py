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


def add(a, b): 
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b) / math.log(a)


def exponent(a, b):
    return a ** b
