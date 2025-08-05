# -----------------------------------------
# STRING METHODS IN PYTHON
# -----------------------------------------

# Get user input
name = input("Enter your name: ")
phone_number = input("Enter your phone #: ")

# Get the length of the name
length = len(name)
print(f"Length of name: {length}")

# Find the position of the first space
index = name.find(" ")
print(f"Index of space in name: {index}")

# Capitalize only the first letter
capitalized_name = name.capitalize()
print(f"Capitalized: {capitalized_name}")

# Convert to uppercase
upper_name = name.upper()
print(f"Uppercase: {upper_name}")

# Convert to lowercase
lower_name = name.lower()
print(f"Lowercase: {lower_name}")

# Check if name is all digits
is_digits = name.isdigit()
print(f"Is name all digits? {is_digits}")

# Check if name is alphabetic (no spaces or numbers)
is_alpha = name.replace(" ", "").isalpha()
print(f"Is name alphabetic? {is_alpha}")

# Count number of spaces in phone number
space_count = phone_number.count(" ")
print(f"Spaces in phone number: {space_count}")

# Remove dashes from phone number
clean_number = phone_number.replace("-", "")
print(f"Cleaned phone number: {clean_number}")


# -------------------------------
#        USERNAME VALIDATION
# -------------------------------

username = input("Enter a username: ")

# Check if username is longer than 12 characters
if len(username) > 12:
    print("Your name can't be more than 12 characters")

# Check if username contains any spaces
elif " " in username:
    print("Your username can't contain spaces")

# Check if username contains only alphabetic characters (no digits or symbols)
elif not username.isalpha():
    print("Your username can't contain digits or symbols")

# All checks passed
else:
    print(f"Welcome {username}!")
