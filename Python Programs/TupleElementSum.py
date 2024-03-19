# Exercise 1
# build your own function which can add each elements present in tuple
# 2 tuple as input with equal length & sum of element wise

# solution 1
def tuple_element_sum():
    try:
        tuple1_input = input("Enter a tuple separated by spaces:\n")
        tuple2_input = input("Enter another tuple separated by spaces:\n")
        tuple1 = tuple(map(int, tuple1_input.split()))
        tuple2 = tuple(map(int, tuple2_input.split()))

        if len(tuple1) != len(tuple2):
            raise ValueError("Both tuple must have equal length")

        sum_tuple = tuple(x + y for x, y in zip(tuple1, tuple2))
        return sum_tuple
    except IndexError:
        print("Please enter a valid tuple")


result = tuple_element_sum()
if result:
    print("Element wise sum of tuple", result)

# Solution2
def add_tuples(tuple1, tuple2):
    """
    Add each element of two tuples and return a new tuple with the sum of corresponding elements.
    """
    if len(tuple1) != len(tuple2):
        return None  # Return None if the tuples are not of equal length

    result = tuple(x + y for x, y in zip(tuple1, tuple2))
    return result

def main():
    # Ask the user to input two tuples
    tuple1_str = input("Enter elements of the first tuple separated by commas: ")
    tuple2_str = input("Enter elements of the second tuple separated by commas: ")

    # Convert the input strings into tuples
    tuple1 = tuple(map(int, tuple1_str.split(',')))
    tuple2 = tuple(map(int, tuple2_str.split(',')))

    # Check if the tuples are of equal length
    if len(tuple1) != len(tuple2):
        print("Error: Tuples are not of equal length.")
        return

    # Calculate the sum of corresponding elements
    result = add_tuples(tuple1, tuple2)

    # Print the result
    if result is not None:
        print("Sum of corresponding elements:", result)
    else:
        print("Error: Tuples are not of equal length.")

if __name__ == "__main__":
    main()


# Solution3
def add_tuples(tuple1, tuple2):
    """
    Add each element of two tuples and return a new tuple with the sum of corresponding elements.
    """
    if len(tuple1) != len(tuple2):
        return None  # Return None if the tuples are not of equal length

    result = tuple(x + y for x, y in zip(tuple1, tuple2))
    return result

def main():
    # Ask the user to input two tuples
    tuple1_str = input("Enter elements of the first tuple separated by commas: ")
    tuple2_str = input("Enter elements of the second tuple separated by commas: ")

    # Convert the input strings into tuples
    tuple1 = tuple(map(int, tuple1_str.split(',')))
    tuple2 = tuple(map(int, tuple2_str.split(',')))

    # Check if the tuples are of equal length
    if len(tuple1) != len(tuple2):
        print("Error: Tuples are not of equal length.")
        return

    # Calculate the sum of corresponding elements
    result = add_tuples(tuple1, tuple2)

    # Print the result
    if result is not None:
        print("Sum of corresponding elements:", result)
    else:
        print("Error: Tuples are not of equal length.")

# Call the main function to execute the program
main()


# Solution4
def add_tuples(tuple1, tuple2):
    """
    Add each element of two tuples and return a new tuple with the sum of corresponding elements.
    """
    if len(tuple1) != len(tuple2):
        print("Error: Tuples are not of equal length.")
        return None  # Return None if the tuples are not of equal length

    result = tuple(x + y for x, y in zip(tuple1, tuple2))
    return result

# Ask the user to input two tuples
tuple1_str = input("Enter elements of the first tuple separated by commas: ")
tuple2_str = input("Enter elements of the second tuple separated by commas: ")

# Convert the input strings into tuples
tuple1 = tuple(map(int, tuple1_str.split(',')))
tuple2 = tuple(map(int, tuple2_str.split(',')))

# Calculate the sum of corresponding elements
result = add_tuples(tuple1, tuple2)

# Print the result
if result is not None:
    print("Sum of corresponding elements:", result)


# Solution5
def add_tuples(tuple1, tuple2):
    # Check if both tuples have equal length
    if len(tuple1) != len(tuple2):
        return "Error: Tuples must be of equal length"

    # Initialize an empty list to store the sum of corresponding elements
    result = []

    # Iterate through each element of the tuples and add them element-wise
    for i in range(len(tuple1)):
        result.append(tuple1[i] + tuple2[i])

    # Convert the result list to a tuple and return
    return tuple(result)

# Example usage:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print("Sum of tuples:", add_tuples(tuple1, tuple2))  # Output: (5, 7, 9)


# Solution6
class TupleAdder:
    def __init__(self):
        pass

    def add_tuples(self, tuple1, tuple2):
        """
        Add each element of two tuples and return a new tuple with the sum of corresponding elements.
        """
        if len(tuple1) != len(tuple2):
            print("Error: Tuples are not of equal length.")
            return None  # Return None if the tuples are not of equal length

        result = tuple(x + y for x, y in zip(tuple1, tuple2))
        return result

    def run(self):
        # Ask the user to input two tuples
        tuple1_str = input("Enter elements of the first tuple separated by commas: ")
        tuple2_str = input("Enter elements of the second tuple separated by commas: ")

        # Convert the input strings into tuples
        tuple1 = tuple(map(int, tuple1_str.split(',')))
        tuple2 = tuple(map(int, tuple2_str.split(',')))

        # Calculate the sum of corresponding elements
        result = self.add_tuples(tuple1, tuple2)

        # Print the result
        if result is not None:
            print("Sum of corresponding elements:", result)


# Create an instance of the TupleAdder class and run the program
tuple_adder = TupleAdder()
tuple_adder.run()


# Solution7
def tuple_element_sum():
    try:
        tuple1_input = input("Enter a tuple separated by spaces:\n")
        tuple2_input = input("Enter another tuple separated by spaces:\n")
        tuple1 = tuple(map(int, tuple1_input.split()))
        tuple2 = tuple(map(int, tuple2_input.split()))

        if len(tuple1) != len(tuple2):
            raise ValueError("Both tuples must have equal length")

        sum_tuple = tuple(x + y for x, y in zip(tuple1, tuple2))
        return sum_tuple
    except ValueError as ve:
        print("Error:", ve)


result = tuple_element_sum()
if result:
    print("Element-wise sum of tuples:", result)





