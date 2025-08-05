# -----------------------------------------
# CONDITIONAL EXPRESSION (TERNARY OPERATOR)
# -----------------------------------------
# Syntax: value_if_true if condition else value_if_false
# Used as a shorter version of an if-else statement

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

# Print whether the number is positive or negative
print("Positive" if num > 0 else "Negative")

# Assign "EVEN" or "ODD" based on whether num is divisible by 2
result = "EVEN" if num % 2 == 0 else "ODD"
print(f"{num} is {result}")

# Get maximum and minimum between a and b
max_num = a if a > b else b
min_num = a if a < b else b
print(f"Max: {max_num}, Min: {min_num}")

# Determine age category
status = "Adult" if age >= 18 else "Child"
print(f"Status: {status}")

# Check if temperature is hot or cold
weather = "HOT" if temperature > 20 else "COLD"
print(f"Weather: {weather}")

# Determine access level based on user role
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(f"Access Level: {access_level}")
