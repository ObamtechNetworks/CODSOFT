#!/usr/bin/python3
"""this is main entry point for all other modules of the calculator"""



from exit_handler import handle_exit
from utils import clear_screen
from start_info import logo, message
from calc_func import my_calculator

# WELCOME MESSAGE
print(message)

user_input = input("Hit 'enter key' to begin: OR 'exit' to quit: ").lower().strip()
if user_input == '':
    clear_screen()
    print(logo)
    my_calculator()
elif user_input == "exit":
    handle_exit()
else:
    clear_screen()
    print("You entered an invalid input, starting calculator anyways...")
    print(logo)
    my_calculator()
