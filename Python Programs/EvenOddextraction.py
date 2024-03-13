# Write a Python program to create a new list containing only the even numbers or only the odd numbers from a given
# list.

#Solution1
# Given list
given_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

# Function to filter even or odd numbers
def filter_numbers(lst, even=True):
    if even:
        return [num for num in lst if num % 2 == 0]
    else:
        return [num for num in lst if num % 2 != 0]

# Ask the user for choice
choice = input("Enter 'even' to get even numbers, 'odd' to get odd numbers: ")

# Check user's choice and filter numbers accordingly
if choice.lower() == 'even':
    new_list = filter_numbers(given_list, even=True)
    print("New list with even numbers:", new_list)
elif choice.lower() == 'odd':
    new_list = filter_numbers(given_list, even=False)
    print("New list with odd numbers:", new_list)
else:
    print("Invalid choice! Please enter 'even' or 'odd'.")



#Solution2
# Initialize empty lists to store numbers
numbers = []

# Input loop
print("Enter numbers to create a list (press Enter without typing anything to finish):")
while True:
    num_input = input("Enter a number (or press Enter to finish): ")
    if num_input == "":
        break
    try:
        num = int(num_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Prompt user for choice
while True:
    choice = input("Do you want to create a new list containing even (E) or odd (O) numbers? ").strip().upper()
    if choice in ['E', 'O']:
        break
    else:
        print("Invalid choice! Please enter 'E' for even numbers or 'O' for odd numbers.")

# Create new list based on user's choice
new_list = []
if choice == 'E':
    new_list = [num for num in numbers if num % 2 == 0]
else:
    new_list = [num for num in numbers if num % 2 != 0]

# Print the new list
if new_list:
    print(f"New list containing only {'even' if choice == 'E' else 'odd'} numbers:", new_list)
else:
    print("No numbers of the specified type found in the list.")

