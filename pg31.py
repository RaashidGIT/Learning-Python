# Aim: Encrypt and decrypt a message using a simple substitution cipher with shuffled characters.
# This code is beginner-friendly and demonstrates lists, loops, and string indexing.

import random
import string

# Create a list of all characters (space + punctuation + digits + letters)
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

# Create a shuffled copy for the encryption key
key = chars.copy()
random.shuffle(key)

# ENCRYPTION
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

# Replace each character with its corresponding character from the shuffled key
for letter in plain_text:
    index = chars.index(letter)      # Find the index of the original character
    cipher_text += key[index]        # Append the encrypted character using the key

print(f"Original message : {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPTION
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

# Reverse the encryption process using the shuffled key
for letter in cipher_text:
    index = key.index(letter)        # Find the index in the shuffled key
    plain_text += chars[index]       # Get the original character from chars

print(f"Encrypted message: {cipher_text}")
print(f"Original message : {plain_text}")
