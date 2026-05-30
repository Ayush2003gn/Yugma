from core.ui.cli.parser import cli_parser as parser
from core.action import action_manager as action

def test_add_task_flow():

    parsed = parser.parse_command(
        'add -t "Learn Python"'
    )
    print(parsed)
    result = action.decision_action(parsed)
    print(result)
    assert result.success is True