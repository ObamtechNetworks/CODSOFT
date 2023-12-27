#!/usr/bin/python3
"""This module serves as the entry point for the password generatro app"""


from passwd_gen import passwd_machine
from utils import clear_screen, handle_exit
from character_lists import welcome_message, logo
# start from here
print(welcome_message)

begin = input("Hit the 'enter key' to begin! type 'exit' to quit: ").lower()
if begin == "":
    # clear screen
    clear_screen()
    print(logo)
    # call the password machine function
    passwd_machine()
elif begin == "exit":
    handle_exit()
else:
    clear_screen()
    print("You've entered an invalid input, starting program anyways...")
    print(logo)
    # call the password machine function
    passwd_machine()
