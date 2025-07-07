import os

TODO_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

# Save tasks to file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display menu
def show_menu():
    print("\n===== To-Do List App =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as completed")
    print("5. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if not tasks:
                print("No tasks found.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    status = "✅" if task.endswith("[Done]") else "⏳"
                    print(f"{i}. {task.replace(' [Done]', '')} [{status}]")

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number to remove: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            if not tasks:
                print("No tasks to mark.")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number to mark as completed: "))
                    if 1 <= num <= len(tasks):
                        if not tasks[num - 1].endswith("[Done]"):
                            tasks[num - 1] += " [Done]"
                            save_tasks(tasks)
                            print("Task marked as completed.")
                        else:
                            print("Task is already completed.")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

