from core.models.taskapp import TaskApp

def test_page_change_tracking():

    page = TaskApp()

    page.add_page("study")

    assert len(page.changed_pages) == 1