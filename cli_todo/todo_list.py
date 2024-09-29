# Program requirements:
# Menu, add new tasks, view all tasks, Delete tasks, Exit application
# Use list for the task storage
from typing import List


class Task:
    def __init__(self, todo: str, done: bool):
        self.todo = todo
        self.done = done

    def checkTask(self):
        self.done = not self.done

    def getTask(self):
        return f"[{'x' if self.done else ' '}] {self.todo}"


def addTask(tasks: List[str], newTask: Task):

    pass


def deleteTask(tasks: List[str]):
    pass


def viewTasks(tasks: List[str]):
    pass


def menu():
    pass
