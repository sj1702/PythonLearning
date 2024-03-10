# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

print("Welcome to the Calculator")
# Display menu options
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Prompt the user to enter choice
choice = input("Enter choice (1/2/3/4): ")

# Prompt the user to enter two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform the calculation based on the user's choice
if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid input")


'''Output 1
Welcome to the Calculator
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice (1/2/3/4): 2
Enter first number: 48
Enter second number: 89
Result: -41.0'''

'''Output 2
Welcome to the Calculator
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice (1/2/3/4): 4
Enter first number: 78
Enter second number: 32
Result: 2.4375'''


'''Output 3
Welcome to the Calculator
Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice (1/2/3/4): 4
Enter first number: 34
Enter second number: 0
Result: Error! Division by zero.'''