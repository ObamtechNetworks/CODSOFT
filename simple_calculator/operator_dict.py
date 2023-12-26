#!/usr/bin/python3
"""This module contains a dictionary list of all available functions
to perform arithmetic operations,this list can be gracefully updated
to add more operation entries
"""


# import functions to add as dict values
from op_funcs import add, sub, div, mul, mod, exp
# CREAT A DICTIONARY with keys as the opeartors and values as functions
operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
    "mod": mod,
    "exp": exp
    }
