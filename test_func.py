import utils

def test_save():
    response = utils.saveTodo("test")
    assert response == "Success"

def test_edit():
    response = utils.editTodo("test12")
    assert response == "Success"

def test_delete():
    response = utils.deleteTodo("test12")
    assert response == "Success"

test_save()
test_edit()
test_delete()