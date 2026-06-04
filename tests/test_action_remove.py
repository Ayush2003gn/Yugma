from core.action.action_manager import decision_action
from core.ui.cli.parser import cli_parser

def test_remove_flow():

    add_cmd = cli_parser.parse_command(
        'add -t "Remove Me"'
    )

    add_result = decision_action(add_cmd)

    uid = add_result.data.uid

    remove_cmd = cli_parser.parse_command(
        f"remove -uid {uid}"
    )

    remove_result = decision_action(remove_cmd)

    assert remove_result.success is True