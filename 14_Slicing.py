#------------------------------------------------------------------
#        EMAIL SLICING
#------------------------------------------------------------------

# Ask the user to enter an email address
email = input("Enter your email: ")

# Extract the part before the '@' symbol (username)
username = email[:email.index("@")]

# Extract the part after the '@' symbol (domain)
domain = email[email.index("@") + 1:]

# Display the results
print(f"Your username is {username} and domain is {domain}")
