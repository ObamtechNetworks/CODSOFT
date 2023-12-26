#!/usr/bin/python3
"""This module defines utility functions
to handle basic utility operations
This can be updated as we proceed
"""


import os


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
