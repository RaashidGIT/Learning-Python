# -----------------------------------------
# PYTHON ARITHMETIC OPERATIONS
# -----------------------------------------

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponent = num1 ** num2

# Display the results
print("\n--- Results ---")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} // {num2} = {floor_division}  # Floor division")
print(f"{num1} % {num2} = {modulus}         # Remainder (modulo)")
print(f"{num1} ** {num2} = {exponent}       # Exponentiation")

# -----------------------------------------
# PYTHON BUILT-IN FUNCTIONS
# -----------------------------------------

# abs() - Absolute value
print("abs(-7) =", abs(-7))  # Output: 7

# max() and min() - Find maximum and minimum
print("max(5, 10, 3) =", max(5, 10, 3))  # Output: 10
print("min(5, 10, 3) =", min(5, 10, 3))  # Output: 3

# round() - Rounds a number
print("round(3.14159, 2) =", round(3.14159, 2))  # Output: 3.14

# pow() - Exponentiation (same as **)
print("pow(2, 3) =", pow(2, 3))  # Output: 8

# len() - Length of string, list, etc.
name = "Python"
print("len('Python') =", len(name))  # Output: 6

# type() - Returns the type of the variable
print("type(42) =", type(42))        # Output: <class 'int'>
print("type(3.14) =", type(3.14))    # Output: <class 'float'>
print("type('hello') =", type('hello'))  # Output: <class 'str'>

# str(), int(), float(), bool() - Type casting
print("str(123) =", str(123))      # Output: '123'
print("int('10') =", int("10"))    # Output: 10
print("float('2.5') =", float("2.5"))  # Output: 2.5
print("bool(0) =", bool(0))        # Output: False

# input() - Get user input
# name = input("Enter your name: ")
# print("Hello", name)

# sum() - Add all elements in an iterable
numbers = [1, 2, 3, 4, 5]
print("sum([1, 2, 3, 4, 5]) =", sum(numbers))  # Output: 15

# sorted() - Sorts a list
unsorted_list = [3, 1, 4, 2]
print("sorted([3, 1, 4, 2]) =", sorted(unsorted_list))  # Output: [1, 2, 3, 4]

# -----------------------------------------
# PYTHON MATH MODULE EXAMPLES
# -----------------------------------------

import math  # Importing the math module

# Constants
print("math.pi =", math.pi)            # π = 3.141592653589793
print("math.e =", math.e)              # e = 2.718281828459045

# Square root
print("math.sqrt(25) =", math.sqrt(25))    # √25 = 5.0

# Power
print("math.pow(2, 3) =", math.pow(2, 3))  # 2^3 = 8.0 (float)
print("2 ** 3 =", 2 ** 3)                  # Same, but returns int if possible

# Absolute value
print("math.fabs(-5) =", math.fabs(-5))    # |−5| = 5.0

# Factorial
print("math.factorial(5) =", math.factorial(5))  # 5! = 120

# Trigonometric functions (radians)
print("math.sin(math.pi / 2) =", math.sin(math.pi / 2))  # sin(90°) = 1.0
print("math.cos(0) =", math.cos(0))                      # cos(0°) = 1.0

# Radians and Degrees conversion
print("math.degrees(math.pi) =", math.degrees(math.pi))  # π radians to degrees = 180°
print("math.radians(180) =", math.radians(180))          # 180° to radians = π

# Logarithm
print("math.log(100, 10) =", math.log(100, 10))   # log base 10 of 100 = 2.0
print("math.log10(1000) =", math.log10(1000))     # log base 10 = 3.0
print("math.log2(8) =", math.log2(8))             # log base 2 = 3.0

# Ceiling and Floor
print("math.ceil(3.1) =", math.ceil(3.1))   # rounds up → 4
print("math.floor(3.9) =", math.floor(3.9)) # rounds down → 3

# -----------------------------------------
# CIRCUMFERENCE OF A CIRCLE
# -----------------------------------------

import math  # To use math.pi

# Input from user
radius = float(input("Enter the radius of the circle: "))

# Formula for circumference
circumference = 2 * math.pi * radius

# Display result
print(f"The circumference of the circle is: {round(circumference, 2)} units")

# -----------------------------------------
# AREA OF A CIRCLE
# -----------------------------------------

import math  # Importing math module for pi

# Input radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate area
area = math.pi * radius ** 2

# Display the result
print(f"The area of the circle is: {round(area, 2)} square units")

# -----------------------------------------
# HYPOTENUSE CALCULATION USING sqrt() AND pow()
# -----------------------------------------

import math  # To access sqrt() and pow()

# Input the lengths of the two shorter sides
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

# Calculate the hypotenuse using Pythagorean theorem
hypotenuse = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

# Display the result
print(f"The hypotenuse is: {round(hypotenuse, 2)} units")
