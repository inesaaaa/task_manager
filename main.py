from tasks.task_manager import TaskManager

def main():
    manager = TaskManager()
    print("Welcome to Task Manager!")
    while True:
        command = input("Enter command (add, list, delete, exit): ").strip()
        if command == "add":
            task = input("Enter a new task: ").strip()
            manager.add_task(task)
        elif command == "list":
            manager.list_tasks()
        elif command == "delete":
            task = input("Enter task to delete: ").strip()
            manager.delete_task(task)
        elif command == "exit":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
