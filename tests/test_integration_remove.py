from core.ui.cli import token
from core import action

def test_remove_task_flow():

    parsed_add = token.parse_command(
        'add -t "Task Remove Test"'
    )

    add_result = action.execute_command(parsed_add)

    task_id = add_result["data"]["iid"]

    parsed_remove = token.parse_command(
        f'remove -id {task_id}'
    )

    remove_result = action.execute_command(parsed_remove)

    assert remove_result["success"] is True