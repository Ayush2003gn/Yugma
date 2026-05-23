from core.ui.cli import token
from core import action

def test_mark_done_flow():

    parsed_add = token.parse_command(
        'add -t "Done Test"'
    )

    add_result = action.execute_command(parsed_add)

    task_id = add_result["data"]["internal_id"]

    parsed_done = token.parse_command(
        f'mark_done -id {task_id}'
    )

    done_result = action.execute_command(parsed_done)

    assert done_result["success"] is True