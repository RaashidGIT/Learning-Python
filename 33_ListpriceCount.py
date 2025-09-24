# ----- EXAMPLE -----
def net_price(list_price, discount=0, tax=0.05):
    # Calculate net price after applying discount and tax
    # discount and tax are optional with default values
    return list_price * (1 - discount) * (1 - tax)

# Examples:
# print(net_price(500))          # No discount, default tax
# print(net_price(500, 0.1))     # 10% discount, default tax
# print(net_price(500, 0.1, 0))  # 10% discount, no tax


# ----- EXERCISE -----
import time

def count(end, start=0):
    # Counts from start to end, printing each number with a 1-second pause
    for x in range(start, end + 1):
        print(x)
        time.sleep(1)
    print("DONE!")

# Examples:
# count(10)       # Counts 0 to 10
# count(30, 15)   # Counts 15 to 30
