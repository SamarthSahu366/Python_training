def manage_todo():
    todo_list = {}

    while True:
        print("\nTo-Do List Manager:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Remove Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':  # Add task
            task = input("Enter task description: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            todo_list[task] = priority
            print(f"Task '{task}' added.")
            
        elif choice == '2':  # Update task
            task = input("Enter task to update: ")
            if task in todo_list:
                priority = input("Enter new priority (High/Medium/Low): ")
                todo_list[task] = priority
                print(f"Task '{task}' updated.")
            else:
                print("Task not found.")
                
        elif choice == '3':  # Remove task
            task = input("Enter task to remove: ")
            if task in todo_list:
                del todo_list[task]
                print(f"Task '{task}' removed.")
            else:
                print("Task not found.")
        
        elif choice == '4':  # View tasks
            if todo_list:
                for task, priority in todo_list.items():
                    print(f"Task: {task}, Priority: {priority}")
            else:
                print("No tasks in the list.")
        
        elif choice == '5':  # Exit
            break
        else:
            print("Invalid choice. Please try again.")

manage_todo()
