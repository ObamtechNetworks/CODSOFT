#!/usr/bin/python3
"""this module defines the core logic for the
rock paper scissors game
"""


import random
import sys
from art import rock, paper, scissors
from utils import input_to_int, prompt_validation, \
    clear_screen, animate_options, display_choices

# store scores globally
scores = {"player1": 0, "player2": 0}
# constants
ROCK, PAPER, SCISSORS = 0, 1, 2

# winning combinations -> rock wins scissors, scissors wins..like so...
winning_combinations = [
    (ROCK, SCISSORS),
    (SCISSORS, PAPER),
    (PAPER, ROCK)]

# store the rock paper scissors arts in list
CHOICE_ARTS = [rock, paper, scissors]
choice_name = ["Rock", "Paper", "Scissors"]


def who_wins(user, computer):
    if (user, computer) in winning_combinations:
        scores["player1"] += 1
        print(f"You win!")
    elif (computer, user) in winning_combinations:
        scores["player2"] += 1
        print("You lost!")
    else:
        print("It's a draw!")


def start_game():
    playon = True
    GAME_ROUNDS = 1
    while playon:
        # get user's input and convert user's input to integer
        print(f"ROUND: {GAME_ROUNDS}")
        while True:
            user_choice = input_to_int(
                """What do you choose? Type
                --> 0 for Rock
                --> 1 for Paper
                --> 2 for Scissors: """)
            if user_choice not in [0, 1, 2]:
                print("Invalid input!..")
            else:
                break

        # generate random integers
        computer_choice = random.randint(0, 2)
        # some small animations before printing
        animate_options(CHOICE_ARTS)
        # display the choices made
        display_choices(user_choice, computer_choice, choice_name, CHOICE_ARTS)
        # DECISIONS BASED ON GAME RULES and print score
        who_wins(user_choice, computer_choice)

        print("\n====================================")
        # whatever is the case print the scores
        print(
            f'Your score is: {scores["player1"]}\n'
            f'Computer score is: {scores["player2"]}')
        print("====================================\n")
        # ask user if they want to continue playing
        again = prompt_validation(
            'Do you want to play another round? "Yes", "No": ')

        if again == 'yes':
            clear_screen()
            GAME_ROUNDS += 1
            playon = True
        else:
            clear_screen()
            print("====================================")
            print(
                f'Total Score:\nYOU: {scores["player1"]}\n'
                f'COMPUTER: {scores["player2"]}\n'
                f'TOTAL ROUNDS PLAYED: {GAME_ROUNDS}')
            playon = False
            print("Thank you for playing...! See you again")
            print("====================================")
