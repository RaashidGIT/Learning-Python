# -------------------------------
# Python Banking Program
# -------------------------------

# Function to display the current balance
def show_balance(balance):
    print("*********************")
    print(f"Your balance is ${balance:.2f}")  # formatted to 2 decimal places
    print("*********************")

# Function to handle deposits
def deposit():
    print("*********************")
    amount = float(input("Enter an amount to be deposited: "))  # user enters amount
    print("*********************")
    if amount < 0:  # check for invalid negative amounts
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0  # no deposit is made
    else:
        return amount  # valid deposit

# Function to handle withdrawals
def withdraw(balance):
    print("*********************")
    amount = float(input("Enter amount to be withdrawn: "))  # user enters amount
    print("*********************")

    # Check if withdrawal is greater than balance
    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    # Check for invalid negative withdrawal
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else:
        return amount  # valid withdrawal

# Main program function
def main():
    balance = 0          # initial balance
    is_running = True    # keeps the program running until user exits

    while is_running:
        # Display menu
        print("*********************")
        print("   Banking Program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*********************")
        
        choice = input("Enter your choice (1-4): ")  # get user input

        # Match user choice
        if choice == '1':
            show_balance(balance)         # show current balance
        elif choice == '2':
            balance += deposit()          # add deposit to balance
        elif choice == '3':
            balance -= withdraw(balance)  # subtract withdrawal from balance
        elif choice == '4':
            is_running = False            # exit loop/program
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")

    # Goodbye message when user exits
    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

# Standard Python convention: run main() only if script is executed directly
if __name__ == '__main__':
    main()
