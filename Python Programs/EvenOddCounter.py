# Create a program that takes a list of numbers as input and counts the number of even and odd numbers in the list.
#Solution

# Input list of numbers
numbers = input("Enter a list of numbers separated by spaces: ").split()

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Iterate through each number in the list
for num in numbers:
    try:
        # Convert the input to integer
        num = int(num)
        # Check if the number is even or odd
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    except ValueError:
        # Handle cases where the input is not a valid number
        print(f"Ignoring '{num}'. It's not a valid number.")

# Print the count of even and odd numbers
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)