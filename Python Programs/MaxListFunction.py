# Write a Python function to find the maximum number in a given list

# Solution
def find_maximum(numbers):
    """
    Function to find the maximum number in a given list.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The maximum number in the list.
    """
    return max(numbers)

# Test the function
numbers = [10, 20, 30, 40, 50]
maximum_number = find_maximum(numbers)
print("The maximum number in the list is:", maximum_number)