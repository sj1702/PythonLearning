# Dictionary / Set / Tuple 

# Set
# my_set = {1,2,3}
# UseCase
'''
1. Remove duplicates
2. checking for membership
3. Performing Math Operation
4. Filtering unique element from a sequence
'''

# tuple
# my_tuple = (1,2,3)
# UseCase
'''
1. storing unchangeable data
2. Returning multiple value
3. Unpacking sequence
'''

#Functions performing on Set
my_set = {1,2,3,4,5}
print(my_set)

#add
my_set.add(6)
print(my_set)
my_set.add(7)
print(my_set)

#remove
my_set.remove(3)
print(my_set)

# Union (|) of two or more sets
set1= {1,2,3,4}
set2= {3,4,5,6}
print(set1 | set2)

# Intersection (&) of two or more sets
print(set1 & set2)

#difference (-) of two or more sets
print(set1 - set2)

# Symmetric Diff (^) of two or more sets
print(set1 ^ set2)


#Tuple 

my_tuple = (1,2,3,4,5)
# Accessing Element
print(my_tuple[3])
  
ae,b,c,d,e = my_tuple
print(ae,b,c,d,e)

num_tuple = input("Enter a bunch of int number with space:\n")
input_tuple = tuple(map(int, num_tuple.split()))
print(input_tuple)

