# Write a program for:
# You have to take bunch of  int as input
# convert it in tuple
# check the even numbers
# print the new tuple of even number

# Solution1
# Function to convert list to tuple
def convert_to_tuple(numbers):
    return tuple(numbers)

# Function to filter even numbers
def filter_even(numbers):
    return tuple(filter(lambda x: x % 2 == 0, numbers))

# Ask the user to input integer numbers
input_numbers = input("Enter integer numbers separated by spaces: ")

# Convert input string to list of integers
numbers_list = list(map(int, input_numbers.split()))

# Convert list to tuple
numbers_tuple = convert_to_tuple(numbers_list)

# Filter even numbers
even_numbers = filter_even(numbers_tuple)

# Print the new tuple of even numbers
print("Even numbers in the tuple:", even_numbers)


# Solution2
# Function to convert list to tuple
def convert_to_tuple(numbers):
    return tuple(numbers)


# Function to filter even numbers
def filter_even(numbers):
    return tuple(filter(lambda x: x % 2 == 0, numbers))


# Main function
def main():
    # Ask the user to input integer numbers
    input_numbers = input("Enter integer numbers separated by spaces: ")

    # Convert input string to list of integers
    numbers_list = list(map(int, input_numbers.split()))

    # Convert list to tuple
    numbers_tuple = convert_to_tuple(numbers_list)

    # Filter even numbers
    even_numbers = filter_even(numbers_tuple)

    # Print the new tuple of even numbers
    print("Even numbers in the tuple:", even_numbers)


if __name__ == "__main__":
    main()


# Solution3
# Function to convert input string to tuple of integers
def get_input_and_convert_to_tuple():
    input_numbers = input("Enter integer numbers separated by spaces: ")
    numbers_list = list(map(int, input_numbers.split()))
    return tuple(numbers_list)

# Function to filter even numbers from tuple
def filter_even_numbers(numbers_tuple):
    return tuple(number for number in numbers_tuple if number % 2 == 0)

# Ask for input and convert to tuple
numbers_tuple = get_input_and_convert_to_tuple()

# Filter even numbers
even_numbers = filter_even_numbers(numbers_tuple)

# Print the new tuple of even numbers
print("Even numbers in the tuple:", even_numbers)


