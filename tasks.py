tasks = []

def add_task(task):
    tasks.append({"task": task, "completed": False})
    print(f"Task added: {task}")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✔️" if task["completed"] else "❌"
            print(f"{i}. {task['task']} - {status}")

def complete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")
