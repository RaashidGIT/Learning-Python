# -------------------------------------------------------------
# AIM: To understand and demonstrate how different iterables 
#      (list, tuple, set, string, and dictionary) can be used 
#      in Python with "for loops".
# -------------------------------------------------------------

# 📌 What is an Iterable?
# An iterable is an object/collection that can return its elements 
# one at a time, allowing it to be iterated over in a loop.

# -------------------------
# Examples of Iterables
# -------------------------

# A List - ordered collection of elements
my_list = [1, 2, 3, 4, 5]

# A Tuple - ordered collection, but immutable (cannot be changed)
my_tuple = (1, 2, 3, 4, 5)

# A Set - unordered collection of unique elements
my_set = {"apple", "orange", "banana", "coconut"}

# A String - a sequence of characters
my_name = "Bro Code"

# A Dictionary - stores key-value pairs
my_dictionary = {'A': 1, 'B': 2, 'C': 3}


# -------------------------
# Iterating through a List
# -------------------------
print("Iterating through List:")
for item in my_list:
    print(item)

# -------------------------
# Iterating through a Tuple
# -------------------------
print("\nIterating through Tuple:")
for item in my_tuple:
    print(item)

# -------------------------
# Iterating through a Set
# -------------------------
print("\nIterating through Set:")
for item in my_set:
    print(item)

# -------------------------
# Iterating through a String
# -------------------------
print("\nIterating through String:")
for char in my_name:
    print(char)

# -------------------------
# Iterating through a Dictionary
# -------------------------

# Print only keys
print("\nDictionary Keys:")
for key in my_dictionary:
    print(key)

# Print only values
print("\nDictionary Values:")
for value in my_dictionary.values():
    print(value)

# Print keys and values together
print("\nDictionary Key-Value Pairs:")
for key, value in my_dictionary.items():
    print(f"{key} = {value}")
