#Write a Python program to reverse a given list

#Solution 1
# Prompt the user to enter a list of elements separated by spaces
elements_input = input("Enter a list of elements separated by spaces: ")

# Split the input string into individual elements
elements_list = elements_input.split()

# Convert the list of strings to a list of integers
numbers = [int(element) for element in elements_list]

# Reverse the list using slicing
reversed_numbers = numbers[::-1]

# Print the reversed list
print("Reversed list:", reversed_numbers)



#Solution 2
# Prompt the user to enter the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))

# Initialize an empty list to store the numbers
numbers = []

# Iterate through the range of number of elements and prompt the user to enter each number
for i in range(num_elements):
    number = float(input("Enter number {}: ".format(i+1)))
    numbers.append(number)

# Reverse the list using slicing
reversed_numbers = numbers[::-1]

# Print the reversed list
print("Reversed list:", reversed_numbers)
