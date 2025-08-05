# ---------------------------------------------
# FOR LOOPS in Python
# Execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence, etc.
# ---------------------------------------------

# ---------- EXAMPLE 1 ----------
# Print numbers from 1 to 10
for x in range(1, 11):
    print(x)

# ---------- EXAMPLE 2 ----------
# Print numbers from 10 down to 1 (reversed order)
for x in reversed(range(1, 11)):
    print(x)
print("🎉 Happy New Year!")

# ---------- EXAMPLE 3 ----------
# Print odd numbers from 1 to 10 (step by 2)
for x in range(1, 11, 2):
    print(x)

# ---------- EXAMPLE 4 ----------
# Loop through and print each character in a string
credit_card = "1234-5678-9012-3456"

for char in credit_card:
    print(char)
