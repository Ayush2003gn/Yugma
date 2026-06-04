from core.action.action_manager import decision_action
from core.ui.cli.parser import cli_parser

def test_action_add():

    parsed = cli_parser.parse_command(
        'add -t "Study Python"'
    )

    result = decision_action(parsed)

    assert result.success is True