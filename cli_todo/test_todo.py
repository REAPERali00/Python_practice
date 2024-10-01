import unittest
from todo_list import TaskInventory


class TestTodo(unittest.TestCase):

    def setUp(self):
        self.todo_inventory = TaskInventory()

    def test_menu(self):
        pass

    def test_add(self):
        inventory_len = len(self.todo_inventory.taskList)
        self.todo_inventory.add_task("some task")
        self.assertEqual(
            inventory_len + 1,
            len(self.todo_inventory.taskList),
            "checking if an item was added to invntory",
        )
        self.assertEqual(
            self.todo_inventory.taskList[-1].todo,
            "some task",
            "checking if the correct item was added",
        )

    def test_delete(self):
        inventory_len = len(self.todo_inventory.taskList)
        self.todo_inventory.add_task("delete task")
        self.todo_inventory.delete_task(inventory_len)
        self.assertEqual(
            inventory_len,
            len(self.todo_inventory.taskList),
            "checking if the item was removed to invntory",
        )
        if self.todo_inventory.taskList:
            self.assertNotEqual(
                self.todo_inventory.taskList[-1].todo,
                "delete task",
                "checking if the correct item was removed",
            )

    def test_view(self):
        pass


if __name__ == "__main__":
    unittest.main()
