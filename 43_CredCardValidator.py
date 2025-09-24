# -------------------------------
# Credit Card Validator (Luhn Algorithm)
# -------------------------------
# Algorithm steps:
# 1. Remove any '-' or ' ' from the card number
# 2. Reverse the card number (process from right to left)
# 3. Add all digits in the ODD positions (1st, 3rd, 5th, ...)
# 4. For digits in EVEN positions (2nd, 4th, 6th, ...):
#      - Double them
#      - If the result is two digits (10 or more), add the digits together
#        (e.g., 12 → 1 + 2 = 3)
# 5. Add the totals from steps 3 and 4
# 6. If the final sum is divisible by 10 → VALID card, otherwise INVALID

# Variables to hold sums
sum_odd_digits = 0
sum_even_digits = 0
total = 0

# Step 1: Input and clean the card number
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-", "")  # remove hyphens
card_number = card_number.replace(" ", "")  # remove spaces
card_number = card_number[::-1]             # reverse the string

# Step 2: Add digits in odd positions (right-to-left, so reversed)
for x in card_number[::2]:  # take every other digit starting at index 0
    sum_odd_digits += int(x)

# Step 3: Process digits in even positions
for x in card_number[1::2]:  # take every other digit starting at index 1
    x = int(x) * 2           # double the digit
    if x >= 10:              # if result is two digits
        # Instead of splitting digits, we can add 1 + (x % 10)
        # Example: 12 → (1 + 2) = 3 → same as (1 + (12 % 10))
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# Step 4: Total sum
total = sum_odd_digits + sum_even_digits

# Step 5: Check validity
if total % 10 == 0:
    print("VALID")
else:
    print("INVALID")

#  Test Credit Card Account Numbers
#  ----------------------------------------
# American Express 378282246310005
# American Express 371449635398431
# American Express Corporate 378734493671000
# Australian Bankcard 5610591081018250
# Diners Club 30569309025904
# Diners Club 38520000023237
# Discover 6011111111111117
# Discover 6011000990139424
# JCB 3530111333300000
# JCB 3566002020360505
# MasterCard 5555555555554444
# MasterCard 5105105105105100
# Visa 4111111111111111
# Visa 4012888888881881
