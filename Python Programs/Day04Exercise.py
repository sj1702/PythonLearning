# Sure! Here are five exercises involving lists and two mini-projects utilizing lists with for loops:

# **List Exercises:**

# Exercise 1: Sum of List Elements
# Write a Python program to calculate the sum of all the elements in a given list.

# Solution
# Define a list
numbers = [10, 20, 30, 40, 50]
# Calculate the sum of all the elements in the list using the sum() function
total = sum(numbers)
# Print the sum of all the elements in the list
print("The sum of all the elements in the list is:", total)

'''Output
The sum of all the elements in the list is: 150'''

# Exercise 2: Find the Maximum Number
# Write a Python program to find the maximum number in a given list.

#Solution
# Given list of numbers
numbers = [10, 20, 5, 35, 25]

# Find the maximum number in the list using the max() function
maximum_number = max(numbers)

# Print the maximum number in the list
print("The maximum number in the list is:", maximum_number)

'''Output
The maximum number in the list is: 35'''

# Exercise 3: Reverse a List
# Write a Python program to reverse a given list.

# Solution
# Given list
numbers = [10, 20, 30, 40, 50]

# Reverse the list using the reverse() method
numbers.reverse()

# Print the reversed list
print("Reversed list:", numbers)

'''Output
Reversed list: [50, 40, 30, 20, 10]'''


# Exercise 4: Remove Duplicates
# Write a Python program to remove duplicates from a given list while preserving the order of elements.

#Solution
# Given list
given_list = [3, 6, 8, 3, 4, 6, 9, 2, 8]

# Using a set to store unique elements
unique_elements = set()

# List to store the result
result_list = []

# Loop through the given list
for item in given_list:
    # If the element is not in the set, add it to both the set and the result list
    if item not in unique_elements:
        unique_elements.add(item)
        result_list.append(item)

# Print the result list with duplicates removed while preserving order
print("List with duplicates removed while preserving order:")
print(result_list)

'''#Output
List with duplicates removed while preserving order:
[3, 6, 8, 4, 9, 2]'''


# Exercise 5: List Comprehension
# Write a Python program to create a new list containing only the even numbers from a given list.

#Solution
# Given list
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a new list containing only even numbers
even_numbers = [num for num in given_list if num % 2 == 0]

# Print the new list
print("Original list:", given_list)
print("List containing only even numbers:", even_numbers)

