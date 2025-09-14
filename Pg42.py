# ==========================================================
#  script1.py
# ==========================================================
# This file can be run as a standalone script OR imported into another script.
# Functions (like favorite_food) can be reused when imported,
# and the "main block" only runs when executed directly.

def favorite_food(food):
    # A simple reusable function
    print(f"Your favorite food is {food}")

def main():
    # Main block of code (only runs if script1.py is run directly)
    print("This is script1")
    favorite_food("pizza")
    print("Goodbye!")

# __name__ is a special built-in variable in Python.
# - If this file is run directly: __name__ == "__main__"
# - If this file is imported:     __name__ == "script1"
if __name__ == '__main__':
    main()



# ==========================================================
#  script2.py
# ==========================================================
# This file is intended to be run as a standalone script.
# It IMPORTS script1.py, reusing its functions.
# Notice: because script1 has the "if __name__ == '__main__':" check,
# only its functions are imported, not its main block.

from script1 import *   # imports favorite_food function

def favorite_drink(drink):
    # Another simple function
    print(f"Your favorite drink is {drink}")

# Code below runs IMMEDIATELY when script2.py is run,
# since it's not inside a main() function.
print("This is script2")
favorite_food("sushi")       # function from script1
favorite_drink("coffee")     # function from script2
print("Goodbye!")
