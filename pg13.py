# indexing = accessing elements of a sequence using [] (indexing operator)
#                     [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0])        # Prints the first character: '1'
print(credit_number[0:4])      # Prints the first 4 characters: '1234'
print(credit_number[:4])       # Same as above (default start = 0): '1234'
print(credit_number[4:8])      # Characters from index 4 to 7: '-567'
print(credit_number[4:])       # From index 4 to the end: '-5678-9012-3456'
print(credit_number[-1])       # Last character: '6'
print(credit_number[-4:])      # Last 4 characters: '3456'
print(credit_number[::2])      # Every second character from start: '1357-01-35'
print(credit_number[::3])      # Every third character from start: '14780-46'

#-------------------------------------------------------------------------
# EXERCISE 1 - Mask Credit Card Number
#-------------------------------------------------------------------------
credit_number = "1234-5678-9012-3456"

# Get the last 4 digits
last_digits = credit_number[-4:]

# Print masked credit number
print(f"XXXX-XXXX-XXXX-{last_digits}")

#-------------------------------------------------------------------------
# EXERCISE 2 - Reverse the credit card number
#-------------------------------------------------------------------------

credit_number = "1234-5678-9012-3456"

# Reverse the entire string using slicing [start:stop:step]
credit_number = credit_number[::-1]

# Print the reversed string
print(credit_number)
