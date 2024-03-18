def calculate_bmi(weight, height):
    return weight / (height ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"


def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("Please enter valid values for weight and height.")
        else:
            bmi = calculate_bmi(weight, height)
            print("Your BMI is:", round(bmi, 2))
            print("You are classified as:", classify_bmi(bmi))
    except ValueError:
        print("Please enter valid numeric values for weight and height.")


if __name__ == "__main__":
    main()



'''Output 1
Enter your weight in kilograms: 60
Enter your height in meters: 1.6
Your BMI is: 23.44
You are classified as: Normal weight'''


'''Output 2
Enter your weight in kilograms: 78
Enter your height in meters: 5feet
Please enter valid numeric values for weight and height.'''
