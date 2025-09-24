# -------------------------------
# Hangman in Python
# -------------------------------
# Features:
# - Random word from a list of animals
# - Guess one letter at a time
# - Wrong guesses add parts to the stick figure
# - Win if you guess the word before figure is complete
# -------------------------------

import random

# Dictionary of ASCII art for the hangman (wrong guesses: 0–6)
hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" o ",
        "   ",
        "   "),
    2: (" o ",
        " | ",
        "   "),
    3: (" o ",
        "/| ",
        "   "),
    4: (" o ",
        "/|\\",
        "   "),
    5: (" o ",
        "/|\\",
        "/  "),
    6: (" o ",
        "/|\\",
        "/ \\")
}

# A tuple of animal words to guess
words = (
    "aardvark", "alligator", "antelope", "bear", "cat", "dog", "elephant",
    "fox", "giraffe", "hippopotamus", "jaguar", "kangaroo", "lion", "monkey",
    "octopus", "panda", "rabbit", "snake", "tiger", "wolf", "zebra"
)

# Display the current hangman drawing
def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

# Display the current progress (hint with underscores)
def display_hint(hint):
    print(" ".join(hint))

# Display the final answer (when game ends)
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)           # pick a random word
    hint = ["_"] * len(answer)              # underscores for hidden letters
    wrong_guesses = 0                       # number of incorrect guesses
    guessed_letters = set()                 # keep track of letters guessed
    is_running = True

    # Main game loop
    while is_running:
        display_man(wrong_guesses)          # draw hangman
        display_hint(hint)                  # show current word progress
        guess = input("Enter a letter: ").lower()

        # Validate guess (must be a single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        # If guess is correct, reveal in hint
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1  # add part of hangman

        # Win condition (all letters guessed)
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN! 🎉")
            is_running = False

        # Lose condition (too many wrong guesses)
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE! 💀")
            is_running = False

# Run game
if __name__ == "__main__":
    main()
