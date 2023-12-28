#!/usr/bin/python3
"""this module contains utility functions
that handles various aspects of the program
such as exit, clear screen, input validation etc
"""


import os
import sys
import time
import random


def handle_exit():
    """exits the program with a message"""
    print("Thank you for using this program, hope to see you again!...")
    sys.exit(0)


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


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
            user_input = input(message).strip()
            if user_input.startswith('-'):
                raise ValueError("Please enter a postive number!")
            result = int(user_input)
            if result < 0:
                raise ValueError("Please enter a postive number!")
            return result
        except ValueError as e:
            print(f"Error: invalid input")


def prompt_validation(prompt):
    """This is a general purpose input validation function
    for 'yes or no'
    """
    while True:
        response = input(prompt).lower().strip()
        if response in ["yes", "no"]:
            return response
            break
        else:
            print("invalid input! please enter 'yes' or 'no'")


def display_choices(user_choice, computer_choice, choice_name, art):
    """Displays the user choice and computer choice with ASCII ARTS"""
    # print the choices name and ascii arts (user and computer)
    clear_screen()

    print(f"\nYou chose: {choice_name[user_choice]}")
    print(art[user_choice])

    print(f"\nComputer: {choice_name[computer_choice]}")
    print(art[computer_choice])


def animate_options(arts):
    """Animate the Rock, Paper, Scissors options."""
    if type(arts) != list:
        pass

    for _ in range(3):  # Display each option three times
        clear_screen()
        art = random.choice(arts)
        print(art, flush=True, end="")
        time.sleep(0.4)  # Adjust the delay as needed

    # clear screen again
    clear_screen()
