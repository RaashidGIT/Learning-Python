# ----- *ARGS Example 1 -----
# *args allows a function to accept any number of positional arguments as a tuple

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 4))  # Output: 10


# ----- *ARGS Example 2 -----
def display_name(*args):
    # Prints all parts of a name (title, first name, middle, etc.)
    print("Hello", end=" ")
    for arg in args:
        print(arg, end=" ")
    print()  # Move to a new line after printing the name

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")


# ----- **KWARGS -----
# **kwargs allows a function to accept any number of keyword arguments as a dictionary

def print_address(**kwargs):
    for value in kwargs.values():
        print(value, end=" ")
    print()  # Move to a new line after printing the address

print_address(street="123 Fake St.",
              pobox="P.O Box 777",
              city="Detroit",
              state="MI",
              zip="54321")


# ----- EXERCISE -----
# Combine *args and **kwargs to print a full shipping label

def shipping_label(*args, **kwargs):
    # Print name/title from args
    for arg in args:
        print(arg, end=" ")
    print()

    # Handle address with optional fields
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    # Print city, state, and zip
    print(f"{kwargs.get('city')}, {kwargs.get('state')} {kwargs.get('zip')}")

# Example usage:
shipping_label("Dr.", "Spongebob", "Squarepants",
               street="123 Fake St.",
               pobox="PO box #1001",
               city="Detroit",
               state="MI",
               zip="54321")
