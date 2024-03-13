# Write a Python program to remove duplicates from a given list while preserving the order of elements.

#Solution 1
#Get input from the user
input_list = input("Enter elements of the list separated by spaces: ").split()

# Initialize an empty list to store unique elements
unique_list = []

# Iterate through the input list
for item in input_list:
    # If the item is not already in the unique list, add it
    if item not in unique_list:
        unique_list.append(item)

# Print the unique list
print("List with duplicates removed while preserving order:")
print(unique_list)




#Solution 2
# Initialize an empty list to store the elements
my_list = []

# Input loop
print("Enter elements of the list (press Enter without typing anything to finish):")
while True:
    element = input("Enter an element (or press Enter to finish): ")
    if element == "":
        break
    my_list.append(element)

# Remove duplicates while preserving the order
seen = set()
new_list = []
for item in my_list:
    if item not in seen:
        seen.add(item)
        new_list.append(item)

# Print the updated list
print("Original list:", my_list)
print("List with duplicates removed:", new_list)

