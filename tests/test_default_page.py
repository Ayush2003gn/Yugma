from core.models.taskapp import TaskApp

def test_default_page_add():

    page = TaskApp()

    page.add_page("work")
    page.set_default("work")

    result = page.add_task(
        "Study Python"
    )

    assert result.success is True