import os

# File to store the tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the text file."""
    if not os.path.exists(TASKS_FILE):
        return []
    
    tasks = []
    with open(TASKS_FILE, "r") as file:
        for line in file:
            # Split the line into status and task description
            parts = line.strip().split(" | ")
            if len(parts) == 2:
                tasks.append({"status": parts[0], "description": parts[1]})
    return tasks

def save_tasks(tasks):
    """Save tasks to the text file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['status']} | {task['description']}\n")

def display_tasks(tasks):
    """Display all tasks with their index, status, and description."""
    if not tasks:
        print("\n📭 Your to-do list is empty!")
        return
    
    print("\n" + "="*40)
    print("📋 YOUR TO-DO LIST")
    print("="*40)
    for index, task in enumerate(tasks, start=1):
        # Use a checkbox symbol based on status
        checkbox = "✅" if task['status'] == "[X]" else "⬜"
        print(f"{index}. {checkbox} {task['description']}")
    print("="*40 + "\n")

def main():
    tasks = load_tasks()
    
    while True:
        print("--- MAIN MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task (Mark as Complete/Incomplete)")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            display_tasks(tasks)
            
        elif choice == '2':
            description = input("Enter the new task: ").strip()
            if description:
                tasks.append({"status": "[ ]", "description": description})
                save_tasks(tasks)
                print("✅ Task added successfully!")
            else:
                print("❌ Task description cannot be empty.")
                
        elif choice == '3':
            display_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the task number to update: "))
                    if 1 <= task_num <= len(tasks):
                        # Toggle status between [ ] and [X]
                        if tasks[task_num - 1]['status'] == "[ ]":
                            tasks[task_num - 1]['status'] = "[X]"
                            print("✅ Task marked as completed!")
                        else:
                            tasks[task_num - 1]['status'] = "[ ]"
                            print("🔄 Task marked as incomplete.")
                        save_tasks(tasks)
                    else:
                        print("❌ Invalid task number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
                    
        elif choice == '4':
            display_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        deleted_task = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"🗑️ Deleted: '{deleted_task['description']}'")
                    else:
                        print("❌ Invalid task number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
                    
        elif choice == '5':
            print("👋 Goodbye! Have a productive day.")
            break
            
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
