#Ways to Input values::

#1
#For String
n = str(input("Enter the value of n? "))

#For Integer
n = int(input("Enter the value of n? "))

#For Float
n = float(input("Enter the value of n? "))



#2
#For Float List
# Prompt the user to enter the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))
# Initialize an empty list to store the elements
elements = []
# Iterate through the range of number of elements and prompt the user to enter each element
for i in range(num_elements):
    number = float(input("Enter number {}: ".format(i+1)))
    elements.append(number)

#For Integer List
# Prompt the user to enter the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))
# Initialize an empty list to store the elements
elements = []
# Iterate through the range of number of elements and prompt the user to enter each element
for i in range(num_elements):
    number = int(input("Enter number {}: ".format(i+1)))
    elements.append(number)

#For String List
# Prompt the user to enter the number of elements in the list
num_elements = int(input("Enter the number of elements in the list: "))
# Initialize an empty list to store the elements
elements = []
# Iterate through the range of number of elements and prompt the user to enter each element
for i in range(num_elements):
    name = str(input("Enter name: ".format(i+1)))
    elements.append(name)


#3
#For Integer List
given_list = [int(x) for x in input("Enter numbers separated by spaces: ").split()]

#For Float List
given_list = [float(x) for x in input("Enter numbers separated by spaces: ").split()]

#For Strings List
given_list = [str(x) for x in input("Enter names separated by spaces: ").split()]


#4
#For Integers List
# Initialize empty lists to store elements
elements = []
# Input loop
print("Enter numbers to create a list (press Enter without typing anything to finish):")
while True:
    input = input("Enter a number (or press Enter to finish): ")
    if input == "":
        break
    try:
        num = int(input)
        elements.append(num)
    except ValueError:
        print("Invalid input! Please enter a valid number.")


#For Float List
# Initialize empty lists to store elements
elements = []
# Input loop
print("Enter numbers to create a list (press Enter without typing anything to finish):")
while True:
    input = input("Enter a number (or press Enter to finish): ")
    if input == "":
        break
    try:
        num = float(input)
        elements.append(num)
    except ValueError:
        print("Invalid input! Please enter a valid number.")


#For String List
# Initialize empty lists to store elements
elements = []
# Input loop
print("Enter names to create a list (press Enter without typing anything to finish):")
while True:
    input = input("Enter a name (or press Enter to finish): ")
    if input == "":
        break
    try:
        name = str(input)
        elements.append(name)
    except ValueError:
        print("Invalid input! Please enter a valid name.")


#5
#For Integers
# Prompt the user to enter a list of numbers separated by spaces
input = input("Enter a list of numbers separated by spaces: ")
# Split the input string into individual numbers
numbers_list = input.split()
# Convert the list of strings to a list of integers
numbers = [int(num) for num in numbers_list]

#For Floats
# Prompt the user to enter a list of numbers separated by spaces
input = input("Enter a list of numbers separated by spaces: ")
# Split the input string into individual numbers
numbers_list = input.split()
# Convert the list of strings to a list of integers
numbers = [float(num) for num in numbers_list]

#For Strings
# Prompt the user to enter a list of names separated by spaces
input = input("Enter a list of names separated by spaces: ")
# Split the input string into individual names
names_list = input.split()
# Convert the list of strings to a list of names
names = [str(name) for name in names_list]

