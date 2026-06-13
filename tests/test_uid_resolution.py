from core.models.taskapp import TaskApp
def test_uid_to_iid_resolution():

    page = TaskApp()

    page.add_page("work")
    page.set_default("work")

    page.add_task("Study")

    iid = page.resolve_uid("Y1")

    assert iid is not None