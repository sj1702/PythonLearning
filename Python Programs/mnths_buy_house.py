"""
Assignment:
   Calculate number of months taken to reach portion of down payment as it will allow user to own home
"""

annual_salary = float(input("The starting annual salary: "))
portion_saved_percent = float(input("The portion of salary to be saved: "))
total_cost = float(input("The cost of your dream home: "))
semi_annual_raise = float(input("semi-annual salary raise: "))
investment_return_rate = float(input("Rate of return for Investment: "))

portion_down_payment = 0.25 * total_cost
monthly_salary=annual_salary/12
current_savings = float(0)
num_months=int(0)

while(current_savings<portion_down_payment):
    portion_saved=monthly_salary*portion_saved_percent
    current_savings = current_savings + (portion_saved + current_savings*(investment_return_rate/12))
    num_months+=1
    if(num_months % 6 == 0):
        monthly_salary = monthly_salary + monthly_salary*semi_annual_raise

print("Number of months:", num_months)

"""
The starting annual salary: 150000
The portion of salary to be saved: 0.44
The cost of your dream home: 1000000
semi-annual salary raise: 0.07
Rate of return for Investment: 0.04
Number of months: 37
"""
