import os

# File to store the tasks
TASK_FILE = 'todo_list.txt'

def load_tasks():
    """Load tasks from the file."""
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as file:
            tasks = [line.strip() for line in file.readlines()]
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASK_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task(task):
    """Add a task to the list."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def remove_task(task):
    """Remove a task from the list."""
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found in the list.")

def view_tasks():
    """View all tasks."""
    tasks = load_tasks()
    if tasks:
        print("Your to-do list:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("Your to-do list is empty.")

def main():
    while True:
        print("\nTo-Do List Options:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '3':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
