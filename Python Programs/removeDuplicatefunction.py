# Write a Python program to remove duplicates from a given list while preserving the order of elements.
#Solution
def remove_duplicates_preserve_order(input_list):
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

'''# Example usage:
input_list = [1, 2, 3, 2, 4, 5, 6, 1]
print(remove_duplicates_preserve_order(input_list))'''
