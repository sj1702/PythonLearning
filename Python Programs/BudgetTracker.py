 Budget tracker
# 1. Add Expense 2. View Expense 3. Exit

#Solution 1
def add_expense(expenses, category, amount):
    expenses.append({"category": category, "amount": amount})
    print(f"Expense of {amount} added to category '{category}'.")

def view_expenses(expenses):
    if expenses:
        print("Expenses:")
        for expense in expenses:
            print(f"Category: {expense['category']}, Amount: {expense['amount']}")
    else:
        print("No expenses recorded yet.")

def main():
    expenses = []
    while True:
        print("\nBudget Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            add_expense(expenses, category, amount)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


#Solution 2
def budget_tracker():
    budget = float(input("Enter your budget: "))
    expenses = []

    while True:
        print("\nBudget Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            expense = float(input("Enter expense amount: "))
            expenses.append(expense)
            print("Expense added successfully.")
        elif choice == "2":
            if expenses:
                print("Expenses:")
                for expense in expenses:
                    print("$", expense)
                print("Total Expenses:", sum(expenses))
            else:
                print("No expenses added yet.")
        elif choice == "3":
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    budget_tracker()


#Solution 3
def budget_tracker():
    expenses = []

    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit Budget Tracker")
        choice = input("Enter your choice:\n")

        if choice == "1":
            expense = float(input("Enter expense amount: \n"))
            expenses.append(expense)
            print("Expense added successfully")
        elif choice == "2":
            if expenses:
                print("Expenses:")
                for i, expense in enumerate(expenses):
                    print(i + 1, "-", "$", expense)
                print("Total Expenses:", sum(expenses))
            else:
                print("No expenses to show")
        elif choice == "3":
            break
        else:
            print("Invalid Input")


budget_tracker()
print("You are out of Budget Tracker")
consent = input("Want to access the Budget Tracker? Y/N\n").upper()
if consent == "Y":
    budget_tracker()
else:
    print("Thanks for using..!!")
