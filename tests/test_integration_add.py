from core.ui.cli import token
from core import action

def test_add_task_flow():

    cmd,arg = token.parse_command(
        'add -t "Learn Python"'
    )
    parsed = token.command_handler(cmd, arg)
    result = action.execute_command(parsed)

    assert result["success"] is True