# Positive or Negative & Zero Number Checker:
# Create a program that takes a list of numbers as input and checks whether each number is positive, negative, or zero.
#Solution
# Prompt the user to enter the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))

# Initialize an empty list to store the numbers
numbers = []

# Iterate through the range of number of elements and prompt the user to enter each number
for i in range(num_elements):
    number = float(input("Enter number {}: ".format(i+1)))
    numbers.append(number)

# Initialize lists to store positive, negative, and zero numbers
positive_numbers = []
negative_numbers = []
zero_numbers = []

# Check each number and categorize them
for num in numbers:
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
    else:
        zero_numbers.append(num)

# Print the categorization results
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
print("Zero:", zero_numbers)


# Even or Odd Number Counter:
# Create a program that takes a list of numbers as input and counts the number of even and odd numbers in the list.
#Solution
# Prompt the user to enter the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))

# Initialize an empty list to store the numbers
numbers = []

# Iterate through the range of number of elements and prompt the user to enter each number
for i in range(num_elements):
    number = float(input("Enter number {}: ".format(i+1)))
    numbers.append(number)

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Iterate through each number in the list
for num in numbers:
    # Check if the number is even or odd
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the count of even and odd numbers
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)


# Grade Calculator:

# Create a program that calculates the grades of students based on their scores. Ask the user to input the scores of multiple students, and then calculate and display their grades (A, B, C, D, or F) based on the following criteria:

# A: 90 or above
# B: 80 - 89
# C: 70 - 79
# D: 60 - 69
# F: below 60