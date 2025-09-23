# -----------------------------------------
# SIMPLE PYTHON CALCULATOR
# -----------------------------------------

# Get operator and numbers from user
operator = input("Enter an operator (+ - * / ** % //): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Perform operation based on operator
if operator == "+":
    result = num1 + num2
    print("Result:", round(result, 3))

elif operator == "-":
    result = num1 - num2
    print("Result:", round(result, 3))

elif operator == "*":
    result = num1 * num2
    print("Result:", round(result, 3))

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", round(result, 3))
    else:
        print("Error: Division by zero is not allowed.")

elif operator == "**":
    result = num1 ** num2
    print("Result:", round(result, 3))

elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        print("Result:", round(result, 3))
    else:
        print("Error: Modulo by zero is not allowed.")

elif operator == "//":
    if num2 != 0:
        result = num1 // num2
        print("Result:", int(result))
    else:
        print("Error: Floor division by zero is not allowed.")

else:
    print(f"'{operator}' is not a valid operator.")
