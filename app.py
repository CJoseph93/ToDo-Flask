from flask import Flask, render_template, request, redirect, url_for
from utils import saveTodo, deleteTodo, editTodo

app = Flask(__name__, template_folder="templates")

todos = []

with open('todos.txt') as savedTodos:
    for line in savedTodos:
        todos.append({"todo": line.strip()})

savedTodos.close()


@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"todo": todo})
    saveTodo(todo)
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    deleteTodo(todos)
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['todo'] = request.form["todo"]
        editTodo(todos)
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

if __name__ == '__main__':
    app.run(debug=True)