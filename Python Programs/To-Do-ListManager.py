# 1. To-Do-List Manager
# Build a simple to-do list manager where user can add,remove,view, mark as complete tasks, Exit To-Do List Manager

#Solution 1
def to_do_list():
    tasks = []
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
                    print(i + 1, "-", task["task"])
                    task_index = int(input("Enter task number to remove:\n")) - 1
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
                    print(i + 1, "-", task["task"])
            else:
                print(" No Task to show")
        elif choice == "4":
            if tasks:
                print("Tasks")
                for i, task in enumerate(tasks):
                    print(i + 1, "-", task["task"])
                    task_index = int(input("Enter task number to Mark as Complete:\n")) - 1
                    if 0 <= task_index < len(tasks):
                        tasks[task_index]["complete"] = True
                        print("Task marked as completed successfully")
                    else:
                        print("Invalid Input")
            else:
                print("No tasks to complete")
        elif choice == "5":
            break
        else:
            print("Invalid Input")


to_do_list()
print("You are out of To-Do-List")
consent = input("Want to access the The To-Do-List? Y/N\n").upper()
if consent == "Y":
    to_do_list()
else:
    print("Thanks for using..!!")



#Solution 2
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task_index):
        if task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Task removed from the to-do list.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for i, task in enumerate(self.tasks):
                status = "✓" if task["completed"] else " "
                print(f"{i + 1}. [{status}] {task['task']}")
        else:
            print("Your to-do list is empty.")

    def mark_as_complete(self, task_index):
        if task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task index.")


def main():
    to_do_list = ToDoList()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task to add: ")
            to_do_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to remove: ")) - 1
            to_do_list.remove_task(task_index)
        elif choice == "3":
            to_do_list.view_tasks()
        elif choice == "4":
            task_index = int(input("Enter task index to mark as complete: ")) - 1
            to_do_list.mark_as_complete(task_index)
        elif choice == "5":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()



#Solution 3
def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added to the to-do list.")

def remove_task(tasks, task_index):
    if task_index < len(tasks):
        del tasks[task_index]
        print("Task removed from the to-do list.")
    else:
        print("Invalid task index.")

def view_tasks(tasks):
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i + 1}. [{status}] {task['task']}")
    else:
        print("Your to-do list is empty.")

def mark_as_complete(tasks, task_index):
    if task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as complete.")
    else:
        print("Invalid task index.")

def main():
    tasks = []
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task to add: ")
            add_task(tasks, task)
        elif choice == "2":
            task_index = int(input("Enter task index to remove: ")) - 1
            remove_task(tasks, task_index)
        elif choice == "3":
            view_tasks(tasks)
        elif choice == "4":
            task_index = int(input("Enter task index to mark as complete: ")) - 1
            mark_as_complete(tasks, task_index)
        elif choice == "5":
            print("Exiting To-Do List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


