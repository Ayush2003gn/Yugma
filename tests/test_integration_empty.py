from core.ui.cli.parser import cli_parser as token

def test_empty_input():

    parsed = token.parse_command("")

    assert parsed.command == "None"