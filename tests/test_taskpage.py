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
    category = "study"
    result = todo.add_page(category)

    assert result["message"] == f"Page is added of category {category}"
    assert len(todo.taskpage) == 1


def test_duplicate_page():
    todo = TaskPage()
    category = "study"

    todo.add_page(category)
    result = todo.add_page(category)

    assert result["message"] == f"Category:{category} is alreay exist"


def test_set_default_page():
    todo = TaskPage()

    todo.add_page("study")
    result = todo.set_default("study")

    assert todo.default.category == "study"
    assert result["message"] == "Category : study is set as default"


# -------------------------------------------------
# category finder tests
# -------------------------------------------------

def test_category_finder_existing():
    todo = TaskPage()
    category = "study"

    todo.add_page(category)
    result = todo.category_finder(category)

    assert result["success"] is True
    assert result["data"].category == category

# -------------------------------------------------
# TASK CREATION TESTS
# -------------------------------------------------

def test_add_task_default_page():
    todo = setup_todo()

    result = todo.add_task("Complete physics")

    assert result["success"] is True
    assert result["data"].task == "Complete physics"



def test_add_task_specific_category():
    todo = TaskPage()
    todo.add_page("work")
    result = todo.add_task("Finish report", category="work")

    assert result["success"] is True
    assert result["data"].task == "Finish report"

def test_add_task_without_default():
    todo = TaskPage()

    result = todo.add_task("Complete physics")
    assert result["success"] is False
    assert result["message"] == "Not set default page or mention page"