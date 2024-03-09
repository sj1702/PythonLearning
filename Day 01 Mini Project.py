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
'''Welcome to Text Converter
Enter the text Milkman
MILKMAN
milkman
Milkman
# Out Put'''

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
print("Welcome to Brand Name Generator")
# Greeting Message
bill = float(input("Enter your Bill amount: "))
tip = float(input("Enter the tip percent: "))
count = int(input("Enter total number of person: "))
# Taking User Input (bill, tip,number of people)

# Calculating the total bill including tip

# Calculating amount for every single  person

# Out Put