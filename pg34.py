# Keyword arguments = arguments passed with parameter names
# - Order doesn't matter
# - Improves readability

# ----- EXAMPLE 1 -----
def hello(greeting, title, first, last):
    # Prints a greeting with title, first and last names
    print(f"{greeting} {title}{first} {last}")

# Using keyword arguments (order can change)
hello("Hello", title="Mr.", last="John", first="James")  # Output: Hello Mr.James John

# ----- EXAMPLE 2 -----
# Print numbers 1 to 10 on one line separated by space (default)
for number in range(1, 11):
    print(number, end=" ")

print()  # New line

# Print numbers 1 to 5 separated by "-" using sep keyword argument in print
print("1", "2", "3", "4", "5", sep="-")  # Output: 1-2-3-4-5

# ----- EXERCISE -----
def get_phone(country, area, first, last):
    # Returns a formatted phone number string
    return f"{country}-{area}-{first}-{last}"

# Using keyword arguments to improve clarity
phone_num = get_phone(country=1, area=123, first=456, last=7890)
print(phone_num)  # Output: 1-123-456-7890
