from core.models.taskpage import TaskPage

def test_default_page_add():

    page = TaskPage()

    page.add_page("work")
    page.set_default("work")

    result = page.add_task(
        "Study Python"
    )

    assert result.success is True