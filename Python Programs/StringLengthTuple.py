# Write a program for:
# You have to take bunch of  string as input
# convert it in tuple
# print the length of each string

# Solution1
def string_length_tuple(*strings):
    """
    Convert a bunch of strings into a tuple and print the length of each string.
    """
    string_tuple = tuple(strings)
    for string in string_tuple:
        print(f"Length of '{string}': {len(string)}")

# Take input strings separated by spaces
input_strings = input("Enter a bunch of strings separated by spaces:\n").split()

# Call the function with the input strings
string_length_tuple(*input_strings)

'''# Output
Enter a bunch of strings separated by spaces:
hello world python programming
Length of 'hello': 5
Length of 'world': 5
Length of 'python': 6
Length of 'programming': 11'''


# Solution2
def string_length_tuple(*strings):
    """
    Convert a bunch of strings into a tuple and print the length of each string.
    """
    string_tuple = tuple(strings)
    lengths = [len(string) for string in string_tuple]  # List comprehension to get lengths of strings
    for i, string in enumerate(string_tuple):
        print(f"Length of '{string}': {lengths[i]}")

# Take input strings separated by spaces
input_strings = input("Enter a bunch of strings separated by spaces:\n").split()

# Call the function with the input strings
string_length_tuple(*input_strings)


# Solution3
def string_length_tuple(*strings):
    """
    Convert a bunch of strings into a tuple and print the length of each string.
    """
    string_lengths = {string: len(string) for string in strings}
    for string, length in string_lengths.items():
        print(f"Length of '{string}': {length}")

# Take input strings separated by spaces
input_strings = input("Enter a bunch of strings separated by spaces:\n").split()

# Call the function with the input strings
string_length_tuple(*input_strings)



# Solution4