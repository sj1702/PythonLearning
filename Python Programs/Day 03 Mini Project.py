# 1. BMI Calculator:
# Create a Body Mass Index (BMI) calculator program. Prompt the user to enter their weight (in kilograms) and height (in meters), then calculate and print their BMI. Additionally, provide a message indicating whether they are underweight, normal weight, overweight, or obese based on the calculated BMI.

# Provide a message indicating the BMI category based on the following ranges:
# Underweight: BMI < 18.5
# Normal weight: 18.5 <= BMI < 25
# Overweight: 25 <= BMI < 30
# Obesity: BMI >= 30

# Solution
print("Welcome to BMI Calculator")

# Prompt the user to enter weight and height
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = float(weight / (height ** 2))

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25:
    category = "Normal weight"
elif 25 <= bmi < 30:
    category = "Overweight"
else:
    category = "Obesity"

# Print BMI and category message
print("Your BMI is:", bmi)
print("Your BMI is: {:.2f}".format(bmi))
print("You are categorized as:", category)

'''Output 1
Welcome to BMI Calculator
Enter your weight in kilograms: 60
Enter your height in meters: 1.6
Your BMI is: 23.437499999999996
Your BMI is: 23.44
You are categorized as: Normal weight'''

'''Output 2
Welcome to BMI Calculator
Enter your weight in kilograms: 78
Enter your height in meters: 1.2
Your BMI is: 54.16666666666667
Your BMI is: 54.17
You are categorized as: Obesity'''


# 2. Simple Calculator
# Write a program to build a simple calculator that can perform addition, subtraction, multiplication and division operations.

# Solution
print("Welcome to the Calculator")

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the menu of operations
print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Prompt the user to choose an operation
choice = input("Enter choice (1/2/3/4): ")

# Perform the selected operation and display the result
if choice == '1':
    result = num1 + num2
    print("Result:", result)
elif choice == '2':
    result = num1 - num2
    print("Result:", result)
elif choice == '3':
    result = num1 * num2
    print("Result:", result)
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero!")
else:
    print("Invalid input")

'''Output 1
Welcome to the Calculator
Enter the first number:  68
Enter the second number:  89

Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice (1/2/3/4):  3
Result: 6052.0'''

'''Output 2
Welcome to the Calculator
Enter the first number:  68
Enter the second number:  0

Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice (1/2/3/4):  4
Error: Division by zero!'''


'''Output 3
Welcome to the Calculator
Enter the first number:  68
Enter the second number:  90

Select operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter choice (1/2/3/4):  2
Result: -22.0'''