import random
import string

length = int(input("Enter the length of the password: "))
upper_case_count = int(input("Enter the number of uppercase letters: "))
lower_case_count = int(input("Enter the number of lowercase letters: "))
number_count = int(input("Enter the number of digits: "))
special_char_count = int(input("Enter the number of special characters: "))

total_characters = upper_case_count + lower_case_count + number_count + special_char_count

if length != total_characters:
    print("Invalid input: Total length does not match the sum of individual counts.")
else:
    if upper_case_count < 0 or lower_case_count < 0 or number_count < 0 or special_char_count < 0:
        print("Invalid input: Counts cannot be negative.")
    else:
        password = ''
        if upper_case_count > 0:
            password += ''.join(random.choices(string.ascii_uppercase, k=upper_case_count))
        if lower_case_count > 0:
            password += ''.join(random.choices(string.ascii_lowercase, k=lower_case_count))
        if number_count > 0:
            password += ''.join(random.choices(string.digits, k=number_count))
        if special_char_count > 0:
            password += ''.join(random.choices(string.punctuation, k=special_char_count))

        password_list = list(password)
        random.shuffle(password_list)
        shuffled_password = ''.join(password_list)
        print("Generated Password:", shuffled_password)
