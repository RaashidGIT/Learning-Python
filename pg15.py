# -----------------------------------------
# FORMAT SPECIFIERS IN PYTHON
# -----------------------------------------

price1 = 3.14159
price2 = -987.65
price3 = 12.34

# Default formatting
print(f"price1 is: ${price1}")
print(f"price2 is: ${price2}")
print(f"price3 is: ${price3}")

# Rounded to 2 decimal places
print(f"Rounded: ${price1:.2f}")

# Allocate 10 spaces, right-aligned
print(f"Right-aligned: ${price3:>10.2f}")

# Left-aligned
print(f"Left-aligned:  ${price3:<10.2f}")

# Center-aligned
print(f"Center-aligned:${price3:^10.2f}")

# Zero padded
print(f"Zero padded:   ${price3:010.2f}")

# Sign for positive and negative
print(f"With sign:      {price1:+.2f} / {price2:+.2f}")

# Sign to leftmost position
print(f"Leftmost sign:  {price2:=+10.2f}")

# Space before positive
print(f"Space before +: {price1: .2f} / {price2: .2f}")

# Comma separator
big_number = 1234567.89
print(f"Comma sep:      ${big_number:,.2f}")

# Percentage format
percentage = 0.875
print(f"As percentage:  {percentage:.1%}")
