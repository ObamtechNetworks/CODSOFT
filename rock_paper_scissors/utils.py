#!/usr/bin/python3
"""this module contains utility functions
that handles various aspects of the program
such as exit, clear screen, input validation etc
"""


def handle_exit():
    """exits the program with a message"""
    print("Thank you for using this program, hope to see you again!...")
    sys.exit(0)


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')
