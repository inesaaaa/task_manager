import unittest
from tasks.task_storage import TaskStorage

class TestTaskStorage(unittest.TestCase):
    def setUp(self):
        self.storage = TaskStorage(file_name="test_tasks.txt")
        with open(self.storage.file_name, "w") as file:
            file.write("")

    def tearDown(self):
        import os
        if os.path.exists(self.storage.file_name):
            os.remove(self.storage.file_name)

    def test_save_task(self):
        self.storage.save_task("Sample task")
        self.assertIn("Sample task", self.storage.load_tasks())

    def test_load_tasks(self):
        self.storage.save_task("Task 1")
        self.storage.save_task("Task 2")
        tasks = self.storage.load_tasks()
        self.assertEqual(len(tasks), 2)

    def test_remove_task(self):
        self.storage.save_task("Task to remove")
        self.storage.remove_task("Task to remove")
        self.assertNotIn("Task to remove", self.storage.load_tasks())

if __name__ == "__main__":
    unittest.main()
