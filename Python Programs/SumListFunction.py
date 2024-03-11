# Write a Python function to calculate the sum of all the elements in a given list.

#Solution
def calculate_sum(numbers):
    """
    Function to calculate the sum of all the elements in a given list.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The sum of all the elements in the list.
    """
    return sum(numbers)

# Test the function
numbers = [10, 20, 30, 40, 50]
total_sum = calculate_sum(numbers)
print("The sum of all the elements in the list is:", total_sum)