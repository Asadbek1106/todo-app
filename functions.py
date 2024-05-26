def get_todo(filepath):
    """ Read a text file and return the list of
    to_do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    """ Write the to_do items in the text file."""
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
