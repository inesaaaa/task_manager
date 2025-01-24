import os

class TaskStorage:
    def __init__(self, file_name="tasks.txt"):
        self.file_name = file_name

    def save_task(self, task):
        with open(self.file_name, "a") as file:
            file.write(task + "\n")

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, "r") as file:
            return [line.strip() for line in file.readlines()]

    def remove_task(self, task):
        tasks = self.load_tasks()
        if task in tasks:
            tasks.remove(task)
            with open(self.file_name, "w") as file:
                file.write("\n".join(tasks) + "\n")
            return True
        return False
