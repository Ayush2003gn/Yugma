from core.models.taskpage import TaskPage


def setup_todo():
    todo = TaskPage()
    todo.add_page("study")
    todo.set_default("study")
    return todo


# -------------------------------------------------
# PAGE TESTS
# -------------------------------------------------

def test_add_page():
    todo = TaskPage()

    result = todo.add_page("study")

    assert result == "Page is added of category study"
    assert len(todo.taskpage) == 1


def test_duplicate_page():
    todo = TaskPage()

    todo.add_page("study")
    result = todo.add_page("study")

    assert result == "The given category is alreay exist"


def test_set_default_page():
    todo = TaskPage()

    todo.add_page("study")
    result = todo.set_default("study")

    assert todo.default.category == "study"
    assert result == "Category : study is set as default"


# -------------------------------------------------
# TASK CREATION TESTS
# -------------------------------------------------

def test_add_task_default_page():
    todo = setup_todo()

    result = todo.add_task("Complete physics")

    assert result["success"] is True
    assert result["task"].task == "Complete physics"


def test_add_task_specific_category():
    todo = TaskPage()

    todo.add_page("study")

    result = todo.add_task("Maths", "study")

    assert result["success"] is True
    assert result["task"].task == "Maths"


def test_add_task_without_default():
    todo = TaskPage()

    result = todo.add_task("Task")

    assert result["success"] is False