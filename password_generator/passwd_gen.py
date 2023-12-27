#!/usr/bin/python3
"""This module defines the password generator program"""


# import dependcies/modules
import logging
from datetime import datetime
from utils import input_to_int, generate_passwd

# Configure logging
logging.basicConfig(
    filename='password_generator.log', level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')


def passwd_machine():
    nr_letters = input_to_int(
        "How many LETTER(s) would you like in your password?\n")
    nr_symbols = input_to_int("How many SYMBOL(s) would you like\n")
    nr_digits = input_to_int("How many NUMBER(s) would you like?\n")

    password_str = generate_passwd(nr_letters, nr_symbols, nr_digits)

    # track the time it was generated
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('\n======================================================')
    print("Your password has been successfully created: ******")

    while True:
        show_password = input(
            "Do you want to reveal the password? (yes/no)\n").lower()
        if show_password == "yes":
            print("================================================")
            print(f"Your password is: {password_str}\n"
                  f"Generated on {timestamp}")
            print("================================================\n")
            print(f"Your password has been successully saved to file")
            break
        elif show_password == "no":
            print("\n=====================================================")
            print(f"Your password has been successfully saved to file")
            print("=====================================================")
            break
        else:
            print("invalid input")

    # save password to file
    try:
        with open("passwd.txt", "a") as passwd:
            passwd.write(
                f"Generated on {timestamp}: Password: {password_str}\n")
        print("password has been to: 'passwd.txt'")
    except Exception as e:
        logging.error(f"Error saving password to file: {e}")
        print(f"Error saving password to file: {e}")


if __name__ == "__main__":
    passwd_machine()
