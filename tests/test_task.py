from core.models.task import Task
import datetime
def sample_task():
    now = datetime.datetime.now()
    return Task(
        "Study",
        "123",
        1,
        now,
        now
    )


def test_mark_done():
    task = sample_task()

    task.mark_done(datetime.datetime.now())

    assert task.done is True


def test_mark_undone():
    task = sample_task()

    task.mark_done(datetime.datetime.now())
    task.mark_undone(datetime.datetime.now())

    assert task.done is False


def test_priority_high():
    task = sample_task()

    task.priority_high(datetime.datetime.now())

    assert task.priority == "High"


def test_priority_medium():
    task = sample_task()

    task.priority_medium(datetime.datetime.now())

    assert task.priority == "Medium"


def test_priority_low():
    task = sample_task()

    task.priority_low(datetime.datetime.now())

    assert task.priority == "Low"


def test_to_dict():
    task = sample_task()

    data = task.to_dict()

    assert type(data) == dict
    assert data["Task"] == "Study"