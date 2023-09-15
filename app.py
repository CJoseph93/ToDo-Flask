from flask import Flask, render_template, request, redirect, url_for
from utils import saveTodo, deleteTodo

app = Flask(__name__, template_folder="templates")

todos = []

with open('todos.txt') as savedTodos:
    for line in savedTodos:
        todos.append({"todo": str(line)})

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

if __name__ == '__main__':
    app.run(debug=True)