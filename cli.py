#from functions import get_todos, write_todos
from modules import functions
import time

now = time.strftime("%b-%d, %Y %H-%M-%S")
print("It is ", now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show") or user_action.startswith("display"):

        todos = functions.get_todos()

        # new_todos = [item.strip(("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()


            new_item = input("Enter new todo: ")
            todos[number] = new_item + "\n"

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            todos.pop(number - 1)

            functions.write_todos(todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Unknown command")


print("bye")


