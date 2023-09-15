def deleteTodo(todos):

    with open('todos.txt', 'w') as fw:
        for todo in todos:
            fw.write(todo.get("todo") + "\n")

    fw.close()

def saveTodo(todo):
    f = open("todos.txt", "a")
    f.write(todo + "\n")
    f.close()