shopping_cart = []
Tomato = 0
Potato = 0
Topato = 0

while True:
    print("\nShopping Cart! State your purpose!")
    ch1 = input("1. Buy\n2. Remove\n3. Exit\nChoose an option: ")

    if ch1 == '3':
        break
    if ch1 == '1':  
        print("\nAvailable Items:")
        print("1. Tomato - $50")
        print("2. Potato - $30")
        print("3. Topato - $35")
        print("4. Exit to main menu")
        ch2 = input("Choose an item to buy: ")

        if ch2 == '1':
            Tomato += 1
            print("Added one Tomato.")
        elif ch2 == '2':
            Potato += 1
            print("Added one Potato.")
        elif ch2 == '3':
            Topato += 1
            print("Added one Topato.")
        elif ch2 == '4':
            continue
        else:
            print("Invalid choice. Try again.")

    elif ch1 == '2': 
        print("\nItems in Cart:")
        print(f"1. Tomato - {Tomato}")
        print(f"2. Potato - {Potato}")
        print(f"3. Topato - {Topato}")
        print("4. Exit to main menu")
        ch2 = input("Choose an item to remove: ")

        if ch2 == '1':
            if Tomato > 0:
                Tomato -= 1
                print("Removed one Tomato.")
            else:
                print("No Tomato in cart to remove.")
        elif ch2 == '2':
            if Potato > 0:
                Potato -= 1
                print("Removed one Potato.")
            else:
                print("No Potato in cart to remove.")
        elif ch2 == '3':
            if Topato > 0:
                Topato -= 1
                print("Removed one Topato.")
            else:
                print("No Topato in cart to remove.")
        elif ch2 == '4':
            continue
        else:
            print("Invalid choice. Try again.")
    else:
        print("Invalid option. Please select 1, 2, or 3.")

TomatoPrice = Tomato * 50
PotatoPrice = Potato * 30
TopatoPrice = Topato * 35
Total = TomatoPrice + PotatoPrice + TopatoPrice

print("\nFinal Cart:")
print(f"Tomato x {Tomato} = ${TomatoPrice}")
print(f"Potato x {Potato} = ${PotatoPrice}")
print(f"Topato x {Topato} = ${TopatoPrice}")
print(f"Total Price = ${Total}")
print("Thank you for shopping!")
