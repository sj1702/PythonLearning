#Sum of List Elements

#Solution1
# Define a list
numbers = [10, 20, 30, 40, 50]

# Initialize a variable to store the sum
total = 0

# Iterate through the list and add each element to the total
for number in numbers:
    total += number

# Print the sum of all the elements in the list
print("The sum of all the elements in the list is:", total)

#Solution 2
# Prompt the user to enter a list of numbers separated by spaces
numbers_input = input("Enter a list of numbers separated by spaces: ")

# Split the input string into individual numbers
numbers_list = numbers_input.split()

# Convert the list of strings to a list of integers
numbers = [int(num) for num in numbers_list]

# Calculate the sum of all the elements in the list
total = sum(numbers)

# Print the sum of all the elements in the list
print("The sum of all the elements in the list is:", total)


#Solution 3
# Prompt the user to enter the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))

# Initialize an empty list to store the numbers
numbers = []

# Iterate through the range of number of elements and prompt the user to enter each number
for i in range(num_elements):
    number = float(input("Enter number {}: ".format(i+1)))
    numbers.append(number)

# Calculate the sum of all the elements in the list
total = sum(numbers)

# Print the sum of all the elements in the list
print("The sum of all the elements in the list is:", total)
