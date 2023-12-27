#!/usr/bin/python3
"""This module defines the password generator program"""


# import dependcies/modules
from datetime import datetime
from utils import input_to_int, generate_passwd


def passwd_machine():
    nr_letters = input_to_int(
        "How many LETTER(s) would you like in your password?\n")
    nr_symbols = input_to_int("How many SYMBOL(s) would you like\n")
    nr_digits = input_to_int("How many NUMBER(s) would you like?\n")

    password_str = generate_passwd(nr_letters, nr_symbols, nr_digits)

    # track the time it was generated
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\nYour password has been successfully created: ******")

    show_password = input(
        "Do you want to reveal the password? (yes/no)\n").lower()

    while True:
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
    with open("passwd.txt", "a") as passwd:
        passwd.write(f"Generated on {timestamp}: Password: {password_str}\n")
    print("password has been to: 'passwd.txt'")


if __name__ == "__main__":
    passwd_machine()
