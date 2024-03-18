'''1. Capital Text Converter:
Create a Python program that takes a user input string and converts 
it to uppercase, lowercase, and title case. '''

# Solution
print("Welcome to Text Converter")
# Greeting Message
n = str(input("Enter the text "))
# Taking User Input 
print(n.upper())
# Converting into Upper Case
print(n.lower())
# Converting into Lower Case
print(n.title())
# Converting into Title Case
'''# Out Put
Welcome to Text Converter
Enter the text Milkman
MILKMAN
milkman
Milkman
'''


'''2. Brand Name Generator:
Create a Python program that takes a user input their birth place name  and pet name. 
After that it will combine them & give the new one as the brand name. '''

# Solution
print("Welcome to Brand Name Generator")
# Greeting Message
bpn = str(input("Enter your BirthPlace Name: "))
pn = str(input("Enter your Pet Name: "))
# Taking User Input (Birth Place Name, Pet Name)
bn = bpn+pn
# Combining them to give the brand name
print("Brand Name for you: " +bn)
'''# Out Put
Welcome to Brand Name Generator
Enter your BirthPlace Name: linux
Enter your Pet Name: world
Brand Name for you: linuxworld'''



'''3. Tip Calculator:
Create a Python program that takes a user input their bill, % of tip they want to give & the number of people.
After that it will give the exact amount which all have to pay, along with tip.'''

# Solution
print("Welcome to Tip Calculator")
# Greeting Message
bill_amount = float(input("Enter your Bill amount: "))
tip_percent = float(input("Enter the tip percent: "))
total_persons = int(input("Enter total number of person: "))
# Taking User Input (bill, tip,number of people)
tip_amount = float((tip_percent * bill_amount) / 100)
total_bill = tip_amount + bill_amount
# Calculating the total bill including tip
amount_each_to_pay = float(total_bill / total_persons)
print(f"Amount each to pay including tip: {Each_pay}")
print(f"Amount each to pay including tip: {amount_each_to_pay:.2f}")
# Calculating amount for every single  person

'''# Out Put1
Welcome to Tip Calculator
Enter your Bill amount:  600
Enter the tip percent:  2
Enter total number of person:  6
Amount each to pay including tip: 102.0
Amount each to pay including tip: 102.0

# Output 2
Welcome to Tip Calculator
Enter your Bill amount:  745.80
Enter the tip percent:  3.5
Enter total number of person:  7
Amount each to pay including tip: 110.27185714285713
Amount each to pay including tip: 110.27'''