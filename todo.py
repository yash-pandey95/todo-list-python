FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.read().splitlines()
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")
        elif choice == "3":
            show_tasks(tasks)
            try:
                idx = int(input("Enter task number to remove: "))
                if 0 < idx <= len(tasks):
                    removed = tasks.pop(idx - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
