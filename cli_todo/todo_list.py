# Program requirements:
# Menu, add new tasks, view all tasks, Delete tasks, Exit application
# Use list for the task storage
from typing import List


class Task:
    def __init__(self, todo: str, done: bool):
        self.todo = todo
        self.done = done

    def check_task(self):
        self.done = not self.done

    def get_printed_task(self):
        return f"[{'x' if self.done else ' '}] {self.todo}"


class TaskInventory:
    def __init__(self):
        self.taskList = list()

    def add_task(self, todo: str):
        self.taskList.append(Task(todo, False))

    def delete_task(self, ind: int):
        if ind in range(len(self.taskList)):
            del self.taskList[ind]
        else:
            print("Index is not in range")

    def view_tasks(self):
        for task in self.taskList:
            print(task.get_printed_task())

    def show_menu(self) -> int:
        opts = ["add a task", "delete a task", "view the tasks", "quit"]
        print("What do you want to do?")
        for i, opt in enumerate(opts):
            print(f"{i+1}. {opt}")
        return len(opts)

    def validate_option(self, choice: int, start: int, end: int) -> bool:
        return choice >= start and choice <= end

    def menu(self) -> int:
        end = self.show_menu()
        choice = int(input("Please choose: "))
        if not self.validate_option(choice, 1, end):
            print("choice was not valid, please choose again: ")
            self.menu()
        return choice


if __name__ == "__main__":
    inventroy = TaskInventory()
    inventroy.add_task("task")
    inventroy.add_task("new task")
    inventroy.delete_task(1)
    inventroy.view_tasks()
