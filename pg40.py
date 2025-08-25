# -------------------------------------------------------------
# AIM: To understand how to use modules in Python.
#
# A module is simply a Python file that contains variables, 
# functions, or classes. It allows us to organize code and 
# reuse it across different programs.
#
# In this example:
#   - example.py → Module file (contains constants and functions)
#   - main.py    → Main program (imports and uses the module)
# -------------------------------------------------------------

# ---------- example.py ----------
# This is our custom module file

pi = 3.14159   # A constant

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def circumference(radius):
    return 2 * pi * radius

def area(radius):
    return pi * radius ** 2


# ---------- main.py ----------
# This is our main program that imports and uses example.py

import example   # Import the entire module

# Access variables and functions from the module
print("PI value:", example.pi)
print("Square of 3:", example.square(3))
print("Cube of 3:", example.cube(3))
print("Circumference of circle (r=3):", example.circumference(3))
print("Area of circle (r=3):", example.area(3))
