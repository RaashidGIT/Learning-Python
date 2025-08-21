# AIM: Python Number Guessing Game
# The program randomly selects a number between lowest_num and highest_num.
# The user tries to guess the number, and the program gives hints
# (too high, too low, or out of range). It also counts the number of guesses.

import random

# ------------------ GAME SETTINGS ------------------
lowest_num = 1       # lower bound
highest_num = 100    # upper bound

# Generate a random number between lowest_num and highest_num
answer = random.randint(lowest_num, highest_num)

# Keep track of guesses
guesses = 0

# Control variable for the loop
is_running = True

# ------------------ GAME INTRO ------------------
print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

# ------------------ MAIN GAME LOOP ------------------
while is_running:

    # Ask for input from the user
    guess = input("Enter your guess: ")

    # Check if input is a digit
    if guess.isdigit():
        guess = int(guess)
        guesses += 1   # count every valid guess attempt

        # Check if guess is out of range
        if guess < lowest_num or guess > highest_num:
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")

        # Compare guess with the answer
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False   # stop game when guessed correctly

    else:
        # If input is not a number
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
