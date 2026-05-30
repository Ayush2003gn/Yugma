"""from core.ui.cli import token
from core import action

def test_priority_flow():

    parsed_add = token.parse_command(
        'add -t "Priority Test"'
    )

    add_result = action.execute_command(parsed_add)

    task_id = add_result["data"]["iid"]

    parsed_priority = token.parse_command(
        f'priority -id {task_id} --p high'
    )

    priority_result = action.execute_command(parsed_priority)

    assert priority_result["success"] is True"""