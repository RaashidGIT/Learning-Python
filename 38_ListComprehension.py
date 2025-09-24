# -------------------------------------------------------------
# AIM: To understand and demonstrate how to use 
#      List Comprehension in Python.
#
# List Comprehension provides a concise way to create lists.
# It is more compact and easier to read than traditional loops.
#
# General Syntax:
#   [expression for value in iterable if condition]
# -------------------------------------------------------------

# --------------------
# EXAMPLE 1: Numbers
# --------------------
# Create new lists by applying operations to numbers
doubles = [x * 2 for x in range(1, 11)]      # Multiply each number by 2
triples = [y * 3 for y in range(1, 11)]      # Multiply each number by 3
squares = [z * z for z in range(1, 11)]      # Square each number

print("Doubles:", doubles)
print("Triples:", triples)
print("Squares:", squares)


# --------------------
# EXAMPLE 2: Strings
# --------------------
fruits = ["apple", "orange", "banana", "coconut"]

# Convert each word to uppercase
uppercase_words = [fruit.upper() for fruit in fruits]

# Extract the first letter of each word
fruit_chars = [fruit[0] for fruit in fruits]

print("\nUppercase Fruits:", uppercase_words)
print("First Letters:", fruit_chars)


# --------------------
# EXAMPLE 3: Filtering Numbers
# --------------------
numbers = [1, -2, 3, -4, 5, -6, 8, -7]

# Separate positive and negative numbers
positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]

# Separate even and odd numbers
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 == 1]

print("\nPositive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)


# --------------------
# EXAMPLE 4: Filtering Grades
# --------------------
grades = [85, 42, 79, 90, 56, 61, 30]

# Only keep grades greater than or equal to 60
passing_grades = [grade for grade in grades if grade >= 60]

print("\nPassing Grades:", passing_grades)
