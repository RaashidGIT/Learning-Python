# -------------------------------
# NESTED LOOP DEMO
# -------------------------------
# A nested loop means a loop inside another loop.
# The inner loop runs completely for each iteration of the outer loop.

# Ask the user for input
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to display: ")

# Outer loop handles rows
for x in range(rows):
    # Inner loop handles columns
    for y in range(columns):
        print(symbol, end="")  # Print symbol without moving to next line
    print()  # Move to next line after each row is printed

