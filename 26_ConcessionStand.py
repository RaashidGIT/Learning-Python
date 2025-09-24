# AIM: Concession Stand Program
# A simple program that displays a menu, allows the user to select food items, 
# stores them in a shopping cart, and calculates the total bill.

# Dictionary: menu items with prices
menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

# List to hold user’s selected items
cart = []

# Total cost initialized to 0
total = 0

# ----------- DISPLAY MENU -----------
print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")  # formatted with width and 2 decimals
print("------------------------")

# ----------- ORDER PROCESSING -----------
while True:
    food = input("Select an item (q to quit): ").lower()  # input made lowercase
    if food == "q":   # quit when user types q
        break
    elif menu.get(food) is not None:   # check if food exists in menu
        cart.append(food)              # add to cart
    else:
        print("Item not available!")   # if food not in menu

# ----------- FINAL BILL -----------
print("------ YOUR ORDER ------")
for food in cart:
    total += menu.get(food)   # accumulate total
    print(food, end=" ")      # print items ordered in one line

print()
print(f"Total is: ${total:.2f}")   # show final cost with 2 decimals
