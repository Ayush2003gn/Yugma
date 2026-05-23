from core.ui.cli import token
from core import action

def test_add_task_flow():

    parsed = token.parse_command(
        'add -t "Learn Python"'
    )

    result = action.execute_command(parsed)

    assert result["success"] is True