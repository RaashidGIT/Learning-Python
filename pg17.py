# -------------------------------
# Python Compound Interest Calculator 
# -------------------------------

print("Hi, I'm a Python Compound Interest Calculator.")

# Initialize variables
principle = 0
rate = 0
time = 0

# Get valid principle amount
while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("Principal can't be less than or equal to zero.")

# Get valid interest rate
while rate <= 0:
    rate = float(input("Enter the annual interest rate (in %): "))
    if rate <= 0:
        print("Rate can't be less than or equal to zero.")

# Get valid time period
while time <= 0:
    time = int(input("Enter the time (in years): "))
    if time <= 0:
        print("Time can't be less than or equal to zero.")

# Calculate compound interest
total = principle * pow((1 + rate / 100), time)

# Display result
print(f"\n Balance after {time} year(s): ${total:.2f}")
