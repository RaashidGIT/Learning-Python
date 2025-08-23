# Aim: Simulate rolling multiple dice and display their ASCII art side-by-side,
# along with the total sum of all dice rolled.
# This code is designed for beginners to understand loops, dictionaries, and basic input/output.

# ● ┌ ─ ┐ │ └ ┘

import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []           # List to hold the rolled dice values
total = 0           # Variable to accumulate the sum of dice
num_of_dice = int(input("How many dice?: "))  # Ask user how many dice to roll

# Roll the dice and add results to the list
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# PRINT VERTICALLY (commented out)
# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

# PRINT HORIZONTALLY: print each line of all dice side-by-side
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")  # Print the current line of the current die
    print()  # Newline after each line of dice

# Calculate total sum of rolled dice
for die in dice:
    total += die

print(f"total: {total}")  # Display the total sum of dice rolled
