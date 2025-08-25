# -------------------------------------------------------------
# AIM: To understand and demonstrate how to use 
#      Membership Operators in Python.
# 
# Membership Operators are used to test whether a value or 
# variable exists inside a sequence (string, list, tuple, set, or dictionary).
#
# Two Membership Operators:
#   1. in       → Returns True if the value exists in the sequence
#   2. not in   → Returns True if the value does NOT exist in the sequence
# -------------------------------------------------------------

# --------------------
# EXAMPLE 1: String
# --------------------
word = "APPLE"   # Secret word

# Ask user to guess a letter
letter = input("Guess a letter in the secret word: ")

# Check if the guessed letter exists in the word
if letter in word:
    print(f"There is a '{letter}' in the word")
else:
    print(f"'{letter}' was not found in the word")


# --------------------
# EXAMPLE 2: Set
# --------------------
students = {"Spongebob", "Patrick", "Sandy"}  # A set of students

student = input("\nEnter the name of a student: ")

# Check if the student is in the class
if student in students:
    print(f"{student} is in this class")
else:
    print(f"{student} is NOT in this class")


# --------------------
# EXAMPLE 3: Dictionary
# --------------------
grades = {
   "Sandy": 'A',
   "Squidward": 'B',
   "Spongebob": 'C',
   "Patrick": 'D'
}

student = input("\nEnter the name of a student: ")

# Check if the student's name is in the dictionary keys
if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} is not in the grade dictionary")


# --------------------
# EXAMPLE 4: Email Validation
# --------------------
email = "BroCode@gmail.com"

# Check if "@" and "." are present in the email string
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
