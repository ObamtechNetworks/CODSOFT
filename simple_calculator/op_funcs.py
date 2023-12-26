#!/usr/bin/python3
"""This module contains the functions for performing
calculations operation via the calculator
"""


import sys


# addition


def add(a, b):
    """returns the sum of two numbers"""
    return a + b


# subtraction
def sub(a, b):
    """returns the difference betweent two numbers"""
    return a - b


# multiplication
def mul(a, b):
    """returns the product result of two numbers"""
    return a * b


# division
def div(a, b):
    """returns the division operation between two inputs"""
    try:
        result = round(a / b, 3)
    except (ZeroDivisionError):
        print("ZeroDivision Error: Cannot divide by Zero")
        sys.exit(1)
    return result


# modulus
def mod(a, b):
    """returns the modulus operation between two values"""
    try:
        result = a % b
    except (ZeroDivisionError):
        print("ZeroDivision Error: Cannot divide by Zero")
        sys.exit(1)
    return result


# exponent or power
def exp(a, b):
    """returns the exponent or power of 'a' raised to 'b'"""
    return a ** b
