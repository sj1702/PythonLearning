# Set & Dictionary

my_set = {1,2,3,4,5}
print(my_set)
 #add
my_set.add(7)
print(my_set)
 #remove
my_set.remove(10)
print(my_set)
 #discard
my_set.discard(10)
print(my_set)
 #clear
my_set.clear()
print(my_set)
 #union
my_set2 = {6,7,8,9}
union_set = my_set.union(my_set2)
print(my_set)


# 1. Set Comprehension

# generate a set containing the squares of numbers from 1 to 10.
# print square of numbers in the range of 1,11
square = {i**2 for i in range(1,11)}
print(square)

# # 2. Set Operation Quiz
print('Define set 1')
user_input= input("Enter an element (write with space):")
user_set_1 = set(user_input.split())
print('Define set 2')
user_input= input("Enter an element (write with space):")
user_set_2 = set(user_input.split())
def set_operation_quiz(user_set_1 = user_set_1, user_set_2 = user_set_2):
  print("Welcome to our program")
  user_input= input("Your Answer for union of set:")
  user_answer_1 = set(user_input.split())
  correct_answer = user_set_1.union(user_set_2)
  if user_answer_1 == correct_answer:
     print("correct answer")
  else:
     print("Incorrect")


#Dictionary

my_dict = {"name": "Nirmal", "age":18, "gender":"M", "State":"WB"}
print(my_dict)

 #get
print(my_dict.get("name"))
 #keys
print(my_dict.keys())
 #values
print(my_dict.values())
 #items
print(my_dict.items())
 #remove
print(my_dict.pop("name"))
print(my_dict)
 #add
my_dict = {"name": "Nirmal", "age":18, "gender":"M", "State":"WB"}
my_dict["name"] = "Raiganj"
print(my_dict)

# 1. Dictionary Manipulation

# Write a function that takes a dictionary as input 
# and returns a new dictionary where the keys and values are swapped.

#Solution 

user_dict={}
num_pairs = int(input("Enter the number of pairs:\n"))
for _ in range(num_pairs):
    key = input("Enter the key:")
    value = input("Enter the value:")
    user_dict[key] = value
    
print(user_dict)
def swap_value(user_dict=user_dict):
     return {value: key for key, value in user_dict.items()}

print(swap_value())

# Dictionary Filtering:
'''Question1
# Write a function that takes a dictionary and a value as input, 
# and returns a new dictionary containing only the key-value pairs 
# where the value matches the input value.'''
#Solution1
def filter_dict(dictionary, value):
    return {key: val for key, val in dictionary.items() if val == value}

user_dict = {}
num_pairs = int(input("Enter the number of pairs:\n"))

# Collecting key-value pairs from the user
for _ in range(num_pairs):
    key = input("Enter the key:")
    value = input("Enter the value:")
    user_dict[key] = value

# Asking user for the value to filter by
filter_value = input("Enter the value for checking")

# Applying the filter function
filtered_dict = filter_dict(user_dict, filter_value)

# Printing the filtered dictionary
for key, val in filtered_dict.items():
    print(f"{key} : {val}")

'''#Output1
Enter the number of pairs:
1
Enter the key: name
Enter the value: Silky
Enter the value for checking: Silky
name : Silky

#Output2
Enter the number of pairs:
3
Enter the key: name
Enter the value: Silky
Enter the key: age
Enter the value: 34
Enter the key: state
Enter the value: NC
Enter the value for checking: Silky'''


# Dictionary Sorting:
'''Question 2# Write a function that takes a dictionary as input 
# and returns a new dictionary where the keys are sorted alphabetically.'''

# Solution1
my_dict = {"name": "Nirmal", "age":18, "gender":"M", "state":"WB"}
print(my_dict)
new_dict = dict(sorted(my_dict.items()))
print(new_dict)
'''# Output1
{'name': 'Nirmal', 'age': 18, 'gender': 'M', 'state': 'WB'}
{'age': 18, 'gender': 'M', 'name': 'Nirmal', 'state': 'WB'}'''

# Solution2
# Ask the user to input key-value pairs for the dictionary
my_dict = {}
num_pairs = int(input("Enter the number of key-value pairs for my_dict: "))
for _ in range(num_pairs):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    my_dict[key] = value

# Print the original dictionary
print("Original Dictionary:", my_dict)

# Sort the keys alphabetically and create a new dictionary
new_dict = dict(sorted(my_dict.items()))

# Print the new dictionary with sorted keys
print("Dictionary with Sorted Keys:", new_dict)

'''# Output2
Enter the number of key-value pairs for my_dict: 3
Enter the key: name
Enter the value: Nirmal
Enter the key: age
Enter the value: 18
Enter the key: gender
Enter the value: M
Original Dictionary: {'name': 'Nirmal', 'age': '18', 'gender': 'M'}
Dictionary with Sorted Keys: {'age': '18', 'gender': 'M', 'name': 'Nirmal'}'''