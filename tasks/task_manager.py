from tasks.task_storage import TaskStorage

class TaskManager:
    def __init__(self):
        self.storage = TaskStorage()

    def add_task(self, task):
        self.storage.save_task(task)
        print(f"Task added: {task}")

    def list_tasks(self):
        tasks = self.storage.load_tasks()
        print("Tasks:")
        for task in tasks:
            print(f"- {task}")

    def delete_task(self, task):
        if self.storage.remove_task(task):
            print(f"Task deleted: {task}")
        else:
            print(f"Task not found: {task}")
