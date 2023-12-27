#!/usr/bin/python3
"""This module contains utility functions to handle parts of the program"""


import random
import os
import sys
from character_lists import letters, digits, symbols


# parse_to_int
def input_to_int(message):
    """This function tries to parse user input to integer
    throws error if any occurred
    Args:
        message:(int)-> converts the message to integer
    Returns:
        returns the converted message
    """
    while True:
        try:
            return int(input(message))  # ask user for input & parse to int
        except ValueError:
            print("Please enter a valid number")


# function to generate random characters for any input
def random_characters(char_set, count):
    """generates random list of characters from a given set/list of char
    it receieves a list of characters to select from: e.g: [a, b, c, d]
    then it receives a count parameter to compute how many values
    are to be picked randomly from the char_set and then returns
    a list of randomly genrated characters from the set

    Args:
        char_set: (list): contains a list of chars to pick randomly from
        count: (int): number of character select randomly from
    Returns:
        returns the randomly generated list of the characters
    """
    return [random.choice(char_set) for _ in range(count)]


# generate_passwd.py
def generate_passwd(n_letters: int, n_symbols: int, n_digits: int) -> int:
    """This function computes the password sequence based
    on user's passoword specification processes it and
    then generates the password for the user
    Args:
        n_letters: (int): takes in the number of letters the user wants
        n_symbols: (int): takes in the number of symbols the uers wants
        n_digits: (int): takes in teh number of digits the user wants
    Returns:
        returns the password generated
    """
    # generate combinations from the list of symbols being imported
    letters_comb = random_characters(letters, n_letters)
    symbols_comb = random_characters(symbols, n_symbols)
    digits_comb = random_characters(digits, n_digits)

    # concatenate combinations list as password list
    password = letters_comb + symbols_comb + digits_comb

    # shuffle the list for more randomness
    random.shuffle(password)

    # return password as string
    return "".join(password)


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def handle_exit():
    """exits the program with a message"""
    print("Thank you for using this program, hope to see you again!...")
    sys.exit(0)
