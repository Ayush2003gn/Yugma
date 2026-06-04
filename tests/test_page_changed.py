from core.models.taskpage import TaskPage

def test_page_change_tracking():

    page = TaskPage()

    page.add_page("study")

    assert len(page.changed_pages) == 1