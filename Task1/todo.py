tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    user_choice = input("Enter your choice: ")

    # Add Task
    if user_choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif user_choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # Remove Task
    elif user_choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"'{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")

    # Exit Program
    elif user_choice == "4":
        print("Exiting To-Do List Program...")
        break

    # Invalid Input
    else:
        print("Invalid choice. Please try again.")