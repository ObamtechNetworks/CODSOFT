#!/usr/bin/python3
"""this module defines the entry point for
the rock paper scissors game
"""

from game import start_game
from art import logo, welcome_message
from utils import clear_screen, handle_exit

print(logo)
print("================= WELCOME =======================")

while True:
    begin = input("Hit the 'enter key' to begin! 'exit or quit' to quit,"
                  " 'help' for HOW TO PLAY: ").lower()
    if begin == "":
        # clear screen
        clear_screen()
        # start the game
        start_game()
        break
    elif begin == "exit" or begin == "quit":
        break
        handle_exit()
    elif begin == "help":
        clear_screen()
        print(welcome_message)
    else:
        clear_screen()
        print("You've entered an invalid input!")
