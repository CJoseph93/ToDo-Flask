def deleteTodo(todos):
    try:
        with open('todos.txt', 'w') as fw:
            for todo in todos:
                fw.write(todo.get("todo") + "\n")
    except:
        return "Error Opening file"
    finally:
        fw.close()
        return "Success"

def saveTodo(todo):
    try:
        f = open("todos.txt", "a")
        f.write(todo + "\n")
    except:
        return "Error opening file"
    finally:
        f.close()
        return "Success"

def editTodo(todos):
    try:
        with open('todos.txt', 'w') as fw:
            for todo in todos:
                fw.write(todo.get("todo") + "\n")
    except:
        return "Error opening file"
    finally:
        fw.close()
        return "Success"