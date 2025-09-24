# Aim: Create a simple Rock-Paper-Scissors game where the user plays against the computer.
# The program takes user input, compares it against a random computer choice,
# determines the winner, and allows repeated play until the user quits.

import random  # Import random module to allow computer to make random choices

options = ("rock", "paper", "scissors")  # Possible choices
running = True  # Control variable for the game loop

while running:
    player = None  # Initialize player choice to None
    computer = random.choice(options)  # Computer randomly selects an option

    # Prompt player until a valid choice is made
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Determine the game outcome
    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the player wants to play again
    if input("Play again? (y/n): ").lower() != "y":
        running = False

print("Thanks for playing!")
