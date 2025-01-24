import unittest
from tasks.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Test task")
        self.assertIn("Test task", self.manager.storage.load_tasks())

    def test_delete_task(self):
        self.manager.add_task("Task to delete")
        self.manager.delete_task("Task to delete")
        self.assertNotIn("Task to delete", self.manager.storage.load_tasks())

    def test_list_tasks(self):
        self.manager.add_task("First task")
        self.manager.add_task("Second task")
        tasks = self.manager.storage.load_tasks()
        self.assertEqual(len(tasks), 2)

if __name__ == "__main__":
    unittest.main()
