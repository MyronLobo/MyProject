from tasks import add_task, view_tasks, complete_task

def main():
    while True:
        print("\nTask Tracker Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to complete: "))
            complete_task(task_number)
        elif choice == "4":
            print("Exiting Task Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
