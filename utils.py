def deleteTodo(todos):
    try:
        with open('todos.txt', 'w') as fw:
            for todo in todos:
                try:
                    fw.write(todo.get("todo") + "\n")
                except:
                    return "Error writing to file"
    except:
        return "Error Opening file"
    finally:
        fw.close()
        return "Success"

def saveTodo(todo):
    try:
        f = open("todos.txt", "a")
        try:
            f.write(todo + "\n")
            return "Success"
        except:
            return "Error Writing to file"
    except:
        return "Error opening file"
    finally:
        f.close()