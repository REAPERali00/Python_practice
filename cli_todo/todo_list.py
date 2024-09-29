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

    def add_task(self):
        print("Enter the task details: ")
        todo = input()
        self.taskList.append(Task(todo, False))

    def delete_task(self, task: Task):
        if task in self.taskList:
            self.taskList.remove(task)
        else:
            print("Task is not in inventory to remove ")

    def view_tasks(self):
        for task in self.taskList:
            print(task.get_printed_task())

    def show_menu(self):
        opts = {"view the tasks", "delete a task", "add a task"}
        print("What do you want to do?")
        for i, opt in enumerate(opts):
            print(f"{i+1}. {opt}")

    def validate_option(self, choice: int, start: int, end: int) -> bool:
        return choice >= start and choice <= end

    def menu(self) -> int:
        self.show_menu()
        choice = int(input("Please choose: "))
        if not self.validate_option(choice, 1, 3):
            print("choice was not valid, please choose again: ")
            self.menu()
        return choice


if __name__ == "__main__":
    inventroy = TaskInventory()
    inventroy.menu()
