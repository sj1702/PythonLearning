# 1. To-Do-List Manager
# Build a simple to-do list manager where user can add,remove,view, mark as complete tasks, Exit To-Do List Manager

#Solution
def to_do_list():
    tasks=[]
    while True:
        print("\n1. Add Tasks\n2. Remove Tasks\n3. View Tasks\n4. Mark Tasks as Complete\n5. Exit To-Do List")
        choice = input("Enter your choice:\n")
        
        if choice == "1":
            task = input("Enter your task: \n")
            tasks.append({"task": task, "completed": False})
            print("Your task has been added successfully")
        elif choice == "2":
            if tasks:
                print("Tasks")
                for i, task in enumerate(tasks):
                    print(i + 1, "-", task ["task"])
                    task_index = int(input("Enter task number to remove:\n")) -1
                    if 0 <= task_index < len(tasks):
                        del tasks[task_index]
                        print("Task removed successfully")
                    else:
                        print("Invalid Input")
            else:
                print("No tasks to remove")
        elif choice == "3":
            if tasks:
                print("Tasks")
                for i, task in enumerate(tasks):
                    print(i + 1, "-", task ["task"])
            else:
                print(" No Task to show")    
        elif choice == "4":
            if tasks:
                print("Tasks")
                for i, task in enumerate(tasks):
                    print(i + 1, "-", task ["task"])
                    task_index = int(input("Enter task number to Mark as Complete:\n")) -1
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]["complete"] = True
                        print("Task marked as completed successfully")
                    else:
                        print("Invalid Input")
            else:
                print("No tasks to complete")
        elif choice =="5":
                 break
        else:
            print("Invalid Input")
to_do_list()
print("You are out of To-Do-List")
consent= input("Want to access the The To-Do-List? Y/N\n").upper()
if consent == "Y":
    to_do_list()
else:
    print("Thanks for using..!!")
    
    
#2nd  Budget tracker 
# 1. Add Expense 2. View Expense 3. Exit

#Solution
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



# 3rd Text based RPG
# player health = 100 
# enemy_health = random.randint (50,100)
# import random

# while 

# damage = random.randint(10,25)
# enemy_health+= damage

import random

def text_based_rpg():
    player_health = 100
    enemy_health = random.randint(50, 100)

    while True:
        print("\n1. Attack Enemy\n2. Exit RPG")
        choice = input("Enter your choice:\n")

        if choice == "1":
            player_damage = random.randint(10, 25)
            enemy_damage = random.randint(5, 20)
            enemy_health -= player_damage
            player_health -= enemy_damage

            print("\nPlayer attacks and deals", player_damage, "damage!")
            print("Enemy attacks and deals", enemy_damage, "damage!")

            print("\nPlayer Health:", player_health)
            print("Enemy Health:", enemy_health)

            if player_health <= 0:
                print("\nYou have been defeated! Game Over.")
                break
            elif enemy_health <= 0:
                print("\nCongratulations! You have defeated the enemy!")
                break

        elif choice == "2":
            print("Exiting RPG. Goodbye!")
            break
        else:
            print("Invalid Input")


text_based_rpg()

print("You are out of RPG")
consent = input("Want to access the RPG again? Y/N\n").upper()
if consent == "Y":
    text_based_rpg()
else:
    print("Thanks for playing..!!")


