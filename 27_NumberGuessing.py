# AIM: Number Guessing Game
# The program generates a random number between a given range.
# The user must guess the number, and the program provides hints 
# whether the guess is too high, too low, or correct. 
# It also counts how many guesses were taken.

import random   # random module for generating random numbers

# Define the range
low = 1
high = 100

# Track number of guesses
guesses = 0

# Generate a random number between low and high
number = random.randint(low, high)

# ------------------ GAME LOOP ------------------
while True:
    # Ask the user for a guess
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1   # increase guess count each attempt

    # Compare the guess with the generated number
    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct!")
        break   # exit loop when correct

# ------------------ RESULT ------------------
print(f"This round took you {guesses} guesses")
