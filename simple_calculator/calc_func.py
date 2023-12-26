#!/usr/bin/python3
"""this is the main module for the calculator program
it connects other modules
"""


# import modules and relevant variables
from operator_dict import operators
from exit_handler import handle_exit
from utils import clear_screen


def my_calculator():
    """computes the respective arithmetic operation based on user input"""

    # boolean to control operations
    game_play = True

    while True:
        decision = input("Welcome! Hit 'enter key' to continue "
                         ">> To quit type: 'exit': ").lower().strip()
        if decision == "exit":
            game_play = False
            handle_exit()
        elif decision == "":
            game_play = True
            break
        else:
            print(f"Invalid input: {decision}")

    print("These are the available operators to begin your Arithmetics")
    # print the operands to the user interface for user to choose from
    for key in operators:
        if key == '+':
            print(f"Addition({key})")
        elif key == '-':
            print(f"Difference({key})")
        elif key == '*':
            print(f"Multiplication({key})")
        elif key == '/':
            print(f"Division({key})")
        elif key == 'mod':
            print(f"Modulus({key})")
        elif key == 'exp':
            print(f"Exponent({key})")

    # creat a variable that ask user for input also handle exceptions
    while True:
        try:
            num1 = float(input("\nEnter first number: ").strip())
            break
        except ValueError:
            print(f"ValueError: Invalid input!")

    while game_play:
        while True:
            try:
                # ask user to pick an operator symbol
                operator = input("Pick an operator from above: ").lower().strip()
                # check if what user chose is in list of operators
                if operator not in operators:
                    clear_screen()
                    print("invalid selection, try again")
                    for keys in operators:
                        print(keys)
                else:
                    break
            except Exception as e:
                print(str(e))

        # show user what they've entered
        print(f"\nYour current input is: {num1}")
        print(f"Your operator is: {operator}")

        # ask user for second or next number and also handle exceptions
        while True:
            try:
                num2 = float(input("Enter next number: ").strip())
                break  # if it is correct break out of loop
            except ValueError:
                print("ValueError: Invalid input!")

        # extract the respective function from the lists of operators
        arithmetic_operation = operators[operator]

        # get the answer or result or output
        answer = arithmetic_operation(num1, num2)

        # print the answer to the console
        print("================================================")
        print(f"RESULT: {num1} {operator} {num2} = {answer}")
        print("================================================")

        # ask if user wants to continue calculating or start new operation
        calc_again = input(f"Type 'y' to continue calculating with {answer}"
                           " 'new' to start afresh, 'exit'  to quit. ").lower().strip()

        # check user's choice
        if calc_again == 'y':
            num1 = answer  # continue calculating with answer
            print(f"\n====== Continuing Calcutions with: {num1}")
            for keys in operators:
                print(keys)
        elif calc_again == 'new':
            clear_screen()  # clear screen and start a new calculation
            print("Starting Afresh...")
            game_play = False
            my_calculator()  # start afresh
        elif calc_again == 'exit':
            game_play = False  # exit stop loop and exit program
            handle_exit()
        else:
            print("Invalid input exiting...")
            break  # exit the program for any other or invalid input


if __name__ == '__main__':
    my_calculator()
