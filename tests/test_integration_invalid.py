from core.ui.cli.parser import cli_parser as token

def test_invalid_command():

    parsed = token.parse_command(
        'abcdefg'
    )

    assert parsed.command == "Invalid"