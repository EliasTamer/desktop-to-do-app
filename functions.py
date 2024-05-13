FILEPATH= "files/todos.txt"

def get_todos(filepath=FILEPATH):
    """"Read a text file and return the list of to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(arg_todos, filepath=FILEPATH):
    """Write the to-do items in the text file"""
    with open(filepath, 'w') as write_file:
        write_file.writelines(arg_todos)