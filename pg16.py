# -------------------------------
# WHILE LOOP BASICS
# -------------------------------
# A while loop keeps running as long as a condition is True

# ---------------- EXAMPLE 1 ----------------
# Keep asking for name until it's not empty

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name!")
    name = input("Enter your name: ")

print(f"Hello {name}!")


# ---------------- EXAMPLE 2 ----------------
# Validate that the entered age is not negative

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative.")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")


# ---------------- EXAMPLE 3 ----------------
# Keep asking for favorite food until user types 'q' to quit

food = input("Enter a food you like (q to quit): ")

while food != "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("Goodbye!")


# ---------------- EXAMPLE 4 ----------------
# Only accept a number between 1 and 10

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid.")
    num = int(input("Enter a number between 1 - 10: "))

print(f"You picked the number {num}.")
