#Solution 1

import random
import string
def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Ask the user for the desired length of the password
password_length = int(input("Enter the length of the password: "))
# Generate and print the password
password = generate_password(password_length)
print("Generated Password:", password)


#Solution 2

import random
import string
# Ask the user for the desired length of the password
password_length = int(input("Enter the length of the password: "))
# Define characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation
# Generate a random password
password = ''.join(random.choice(characters) for _ in range(password_length))
# Print the generated password
print("Generated Password:", password)


#Solution 3

import random
import string
def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    # Define character sets based on user preferences
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Ask the user for the desired length of the password
password_length = int(input("Enter the length of the password: "))
# Ask the user for character preferences
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'
# Generate and print the password
password = generate_password(password_length, use_lowercase, use_uppercase, use_digits, use_special)
print("Generated Password:", password)



#Solution 4
import secrets
import string
def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password using secrets module
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password
# Ask the user for the desired length of the password
password_length = int(input("Enter the length of the password: "))
# Generate and print the password
password = generate_password(password_length)
print("Generated Password:", password)



#Solution 5

import random
import string
def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password using random.sample() function
    password = ''.join(random.sample(characters, length))
    return password
# Ask the user for the desired length of the password
password_length = int(input("Enter the length of the password: "))
# Generate and print the password
password = generate_password(password_length)
print("Generated Password:", password)