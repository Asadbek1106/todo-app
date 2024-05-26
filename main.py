from functions import get_todo, write_todos
import time

now = time.strftime("%b %d, %Y  %H:%M")
print("It is", now)

while True:
    user_input = input("Type add, show, edit, complete or exit: ")

    if user_input.startswith("add"):
        new_todo = user_input[4:]

        todos = get_todo("todos.txt")

        todos.append(new_todo + "\n")

        write_todos("todos.txt", todos)

    elif user_input.startswith("show"):

        todos = get_todo("todos.txt")

        for index, i in enumerate(todos):
            i = i.strip("\n")
            print(f"{index + 1}. {i}")
    elif user_input.startswith("edit"):
        try:
            number = int(user_input[5:])
            number = number - 1

            todos = get_todo("todos.txt")

            another_todo = input("Enter new todo: ")
            todos[number] = another_todo + "\n"

            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")

    elif user_input.startswith("complete"):
        try:
            num = int(user_input[9:])

            todos = get_todo("todos.txt")

            index = num - 1
            todo_removing = todos[index]

            todos.pop(index)

            write_todos("todos.txt", todos)

            print(f"You removed {todo_removing.strip("\n")}.")
        except IndexError:
            print("There is no item in that number.")
    elif user_input.startswith("exit"):
        break
    else:
        print("This command is valid.")

print("Bye!")
