# -----------------------------------------
# if = Do something if a condition is True
# else = Do something else if the above condition(s) are False
# elif = Check another condition if the previous one was False
# -----------------------------------------

# -----------------------------------------
# EXAMPLE 1: Age Check
# -----------------------------------------
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")

# -----------------------------------------
# EXAMPLE 2: Yes/No Response
# -----------------------------------------
response = input("Do you want food (Y/N)?: ")

if response.upper() == "Y":
    print("Have some food")
else:
    print("No food for you!")

# -----------------------------------------
# EXAMPLE 3: Name Check
# -----------------------------------------
name = input("Enter your name: ")

if name == "":
    print("You did not enter your name!")
else:
    print(f"Hello {name}")

# -----------------------------------------
# EXAMPLE 4: Online Status
# -----------------------------------------
online = False

if online:
    print("You are online")
else:
    print("You are offline")
