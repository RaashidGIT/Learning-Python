# wordslist.py --------------------------------------------------------------------------------------------
# A separate file containing the word list for Hangman

words = (
    "aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape",
    "armadillo", "baboon", "badger", "bat", "bear", "beaver", "bee", "bison",
    "boar", "buffalo", "butterfly", "camel", "capybara", "caribou", "cat",
    "caterpillar", "cattle", "cheetah", "chicken", "chimpanzee", "chinchilla",
    "cobra", "cockroach", "coyote", "crab", "crocodile", "crow", "deer",
    "dinosaur", "dog", "dolphin", "donkey", "dove", "dragonfly", "duck",
    "eagle", "eel", "elephant", "falcon", "ferret", "fish", "flamingo", "fly",
    "fox", "frog", "gazelle", "giraffe", "goat", "goldfish", "goose", "gorilla",
    "hamster", "hawk", "hedgehog", "hippopotamus", "horse", "human", "hyena",
    "jaguar", "jellyfish", "kangaroo", "koala", "lemur", "leopard", "lion",
    "llama", "lobster", "monkey", "moose", "mosquito", "mouse", "mule",
    "octopus", "ostrich", "otter", "owl", "ox", "oyster", "panda", "parrot",
    "peafowl", "pelican", "penguin", "pig", "pigeon", "pony", "porcupine",
    "quail", "rabbit", "raccoon", "rat", "raven", "reindeer", "rhinoceros",
    "salmon", "seal", "shark", "sheep", "skunk", "snail", "snake", "sparrow",
    "spider", "squid", "squirrel", "swan", "tiger", "toad", "trout", "turkey",
    "turtle", "vulture", "walrus", "wasp", "weasel", "whale", "wolf", "wombat",
    "woodpecker", "worm", "yak", "zebra"
)

# ------------------------------------------------------------------------------------------------------------

# hangman.py
import random
from wordslist import words   # import words from wordslist.py

# Dictionary of ASCII art for the hangman
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

def display_man(wrong_guesses):
    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("**********")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)   # pick a random word from imported list
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN! 🎉")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE! 💀")
            is_running = False

if __name__ == "__main__":
    main()
