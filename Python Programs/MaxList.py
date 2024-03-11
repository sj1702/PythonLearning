#Write a Python program to find the maximum number in a given list.

#Solution 1
# Prompt the user to enter a list of numbers separated by spaces
numbers_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string into individual numbers
numbers_list = numbers_input.split()

# Convert the list of strings to a list of integers
numbers = [int(num) for num in numbers_list]

# Find the maximum number in the list using the max() function
maximum_number = max(numbers)

# Print the maximum number in the list
print("The maximum number in the list is:", maximum_number)


#Solution 2
# Prompt the user to enter the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))

# Initialize an empty list to store the numbers
numbers = []

# Iterate through the range of number of elements and prompt the user to enter each number
for i in range(num_elements):
    number = float(input("Enter number {}: ".format(i+1)))
    numbers.append(number)

# Find the maximum number in the list using the max() function
maximum_number = max(numbers)

# Print the maximum number in the list
print("The maximum number in the list is:", maximum_number)