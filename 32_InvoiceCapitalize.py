# ----------  EXAMPLE 1  ---------- 
def display_invoice(username, amount, due_date):
    # Prints a simple invoice message with username, amount (formatted to 2 decimals), and due date
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

# Example calls:
# display_invoice("BroCode", 42.50, "01/01")
# display_invoice("JoeSchmo", 100.01, "01/02")


# ----------  EXAMPLE 2  ---------- 
def create_name(first, last):
    # Capitalizes the first and last name and combines them with a space
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)  # Output: Spongebob Squarepants
