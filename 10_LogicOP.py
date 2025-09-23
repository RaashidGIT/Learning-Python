# -----------------------------------------
# LOGICAL OPERATORS
# -----------------------------------------

# and  → True if both conditions are True
# or   → True if at least one condition is True
# not  → Reverses the condition (True becomes False)

# Example variables
temp = 20
sunny = True

# Check temperature using 'or'
if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")

# Check weather using 'not'
if not sunny:
    print("It is cloudy")
else:
    print("It is sunny")

# Age verification using 'and'
age = 25
has_ID = True

if age >= 18 and has_ID:
    print("Access granted.")
else:
    print("Access denied.")
