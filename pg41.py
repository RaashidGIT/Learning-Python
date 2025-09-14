# ---------------- LOCAL SCOPE ----------------
# A variable created inside a function belongs to that function only (local scope).

def func1():
    x = 1  # 'x' is local to func1()
    print(x)  # prints 1

def func2():
    x = 2  # 'x' is local to func2()
    print(x)  # prints 2

func1()  # Output: 1
func2()  # Output: 2


# ---------------- ENCLOSED SCOPE ----------------
# If a function is inside another function (nested), the inner function
# can access variables from the outer (enclosing) function.

def func1():
    x = 1  # 'x' is in the enclosing scope of func2()

    def func2():
        # func2() does not have its own 'x', so it looks into the enclosing scope
        print(x)  # prints 1

    func2()

func1()  # Output: 1


# ---------------- GLOBAL SCOPE ----------------
# A variable declared outside of all functions belongs to the global scope.
# Any function can access it (unless shadowed by a local variable with the same name).

def func1():
    print(x)  # Looks for 'x' in global scope

def func2():
    print(x)  # Looks for 'x' in global scope

x = 3  # 'x' is a global variable

func1()  # Output: 3
func2()  # Output: 3


# ---------------- BUILT-IN SCOPE ----------------
# Python has some names already defined (called built-in scope).
# Example: constants and functions from imported modules can be used directly.

from math import e  # 'e' is the mathematical constant (Euler’s number ≈ 2.718)

def func1():
    print(e)  # prints the built-in constant 'e'

func1()  # Output: 2.718281828459045
