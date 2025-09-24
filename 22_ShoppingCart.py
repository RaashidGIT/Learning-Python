# 🛒 Shopping Cart Program

# Create empty lists to store items and their prices
foods = []
prices = []

# Total price starts at 0
total = 0

# Loop to take user input
while True:
    food = input("Enter a food to buy (or 'q' to quit): ")
   
    if food.lower() == "q":
        break  # Exit the loop when user enters 'q'
    else:
        # Get price for the entered food
        price = float(input(f"Enter the price of {food}: $"))
       
        # Add food and price to respective lists
        foods.append(food)
        prices.append(price)

# Print the final cart
print("\n----- 🧾 YOUR CART -----")
for food, price in zip(foods, prices):
    print(f"{food}: ${price:.2f}")

# Calculate total
total = sum(prices)

print("\nTotal amount: ${:.2f}".format(total))
