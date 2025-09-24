# -------------------------------
# Python Slot Machine 🎰
# -------------------------------
# Features:
# - Start with a balance
# - Place bets
# - Spin 3 symbols
# - Match 3 of the same symbol to win
# - Different symbols have different payouts
# - Game continues until balance is 0 or player quits

import random

# Spin and return 3 random symbols
def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']   # list of slot symbols
    # Randomly pick 3 symbols (could repeat)
    return [random.choice(symbols) for _ in range(3)]

# Display the row in a nice format
def print_row(row):
    print("**************")
    print(" | ".join(row))  # join symbols with |
    print("**************")

# Calculate payout based on result and bet
def get_payout(row, bet):
    # Check if all three symbols are the same
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0  # no match, no payout

def main():
    balance = 100  # starting money

    print("*************************")
    print(" Welcome to Python Slots ")
    print(" Symbols: 🍒 🍉 🍋 🔔 ⭐ ")
    print("*************************")

    # Keep playing while player has money
    while balance > 0:
        print(f"Current balance: ${balance}")

        # Ask player to place bet
        bet = input("Place your bet amount: ")

        # Validate bet input
        if not bet.isdigit():
            print("Please enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        # Subtract bet from balance
        balance -= bet

        # Spin the slot machine
        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        # Calculate payout
        payout = get_payout(row, bet)

        # Show result
        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("Sorry, you lost this round.")

        # Add payout back to balance
        balance += payout

        # Ask if player wants to continue
        play_again = input("Do you want to spin again? (Y/N): ").upper()
        if play_again != 'Y':
            break

    # Game ends
    print("*******************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("*******************************************")

# Run the game
if __name__ == '__main__':
    main()
