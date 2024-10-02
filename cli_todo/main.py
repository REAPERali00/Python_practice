from enum import IntEnum
from todo_list import TaskInventory


def read_value(message: str):
    respond = input(message)
    return (
        respond
        if respond
        else read_value("you must enter a value. please try again.\n" + message)
    )


def exec_choice(inventory: TaskInventory) -> bool:
    choice = inventory.menu()
    match (choice):
        case 1:
            task = read_value("Please enter the task: ")
            inventory.add_task(task)
        case 2:
            inventory.view_tasks()
            task_num = int(read_value("Which task do you want to delete? "))
            inventory.delete_task(task_num - 1)
        case 3:
            inventory.view_tasks()
        case 4:
            print("bye!")
            return False
        case _:
            print("option not found.")
    return True


def main():
    inventory = TaskInventory()
    while exec_choice(inventory):
        pass


if __name__ == "__main__":
    main()
