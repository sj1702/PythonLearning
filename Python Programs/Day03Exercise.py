# Ex-1: Write a program that takes a numeric input representing a student's score and prints out the corresponding
# letter grade according to the following grading scale: A: 90-100 B: 80-89 C: 70-79 D: 60-69 F: Below 60

#Solution
# Prompt the user to enter the student's score
score = float(input("Enter the student's score: "))

# Determine the corresponding letter grade based on the grading scale
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the corresponding letter grade
print("The student's grade is:", grade)


# Ex-2: Write a program that checks whether a given year is a leap year or not. A year is a leap year if it is
# divisible by 4 but not divisible by 100, except if it is also divisible by 400.

# Solution
# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

# Ex-3: Write a program that takes two numbers as input and prints out which one is greater, or if they are equal.

# Solution
# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers and print the result
if num1 > num2:
    print("The first number ({}) is greater than the second number ({}).".format(num1, num2))
elif num1 < num2:
    print("The second number ({}) is greater than the first number ({}).".format(num2, num1))
else:
    print("Both numbers are equal.")


# Ex-4: Write a program that asks the user for their age and checks if they are eligible to vote (age >= 18). Print a
# message indicating whether they can vote or not.
#Solution1
# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Check if the user is eligible to vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

#Solution2
# Prompt the user to enter their age and the eligible voting age
age = int(input("Enter your age: "))
eligible_age = int(input("Enter the eligible voting age: "))

# Check if the user is eligible to vote
if age >= eligible_age:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


# Ex-5:Write a program that converts temperature from Celsius to Fahrenheit or vice versa based on user input. Ask
# the user for the temperature and the desired conversion, then print out the converted temperature.

#Solution
# Prompt the user to enter the temperature
temperature = float(input("Enter the temperature: "))

# Prompt the user to choose the conversion type
print("Choose the conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
conversion_type = int(input("Enter your choice (1/2): "))

# Convert temperature based on user's choice and print the result
if conversion_type == 1:
    converted_temperature = (temperature * 9/5) + 32
    print("The temperature in Fahrenheit is:", converted_temperature)
elif conversion_type == 2:
    converted_temperature = (temperature - 32) * 5/9
    print("The temperature in Celsius is:", converted_temperature)
else:
    print("Invalid choice. Please enter 1 or 2 for conversion.")

