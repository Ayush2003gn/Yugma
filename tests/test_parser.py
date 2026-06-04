from core.ui.cli.parser import cli_parser

def test_parse_add():
    result = cli_parser.parse_command(
        'add -t "Study Python"'
    )

    assert result.command == "add"


def test_parse_invalid():
    result = cli_parser.parse_command(
        "abcdefg"
    )

    assert result.command == "Invalid"