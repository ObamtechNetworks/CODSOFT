#!/usr/bin/python3
"""this module defines the core logic for the
rock paper scissors game
"""

# Write your code below this line 👇

# import random module to generate random integers from 0 to 2
import random
import sys

playon = True
while playon:
    print("Welcome to ROCK PAPER SCISSORS GAME! TRY YOUR LUCK!")
    # get user's input
    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
    # generate random integers
    computer = random.randint(0, 2)
    #convert user's input to integer
    try:
        choice = int(user_input)
    except Exception:
        print("invalid input")
        sys.exit(1)
    
    if choice not in [0, 1, 2]:
        print("Invlaid input")
        sys.exit(1)
    
    # store the rock paper scissors in list
    rock_paper_scissors = [rock, paper, scissors]
    choice_name = ["Rock", "Paper", "Scissors"]
    
    # print(rock_paper_scissors[choice])
	# check if user's input match computer's input based on the index value of in list
    if rock_paper_scissors[choice] == rock_paper_scissors[computer]:
        print("It's a Draw!")
    else:
        print(f"\nYour choice: {choice_name[choice]}")
        print(rock_paper_scissors[choice])
    
        print(f"\nComputer: {choice_name[computer]}")
        print(rock_paper_scissors[computer])

	# DECISIONS BASED ON GAME RULES
    if choice == 0 and computer == 2:
        print("You win!")
    elif choice == 2 and computer == 0:
        print("You lost!")
    if choice == 2 and computer == 1:
    	print("You win!")
    elif choice == 1 and computer == 2:
    	print("You lost!")
    if choice == 1 and computer == 0:
    	print("You win!")
    elif choice == 0 and computer == 1:
    	print("You lost!")
    
    # ask user if they want to continue playing
    again = input('Do you want to play again? "Yes", "No": ').lower()
    if again == "yes":
        playon = True
    else:
        print("Have a great day!")
        playon = False