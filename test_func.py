import utils

def test_save():
    response = utils.saveTodo("test")
    assert response == "Success"

def test_delete():
    response = utils.deleteTodo("test")
    assert response == "Success"

test_save()
test_delete()