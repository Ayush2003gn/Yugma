from core.ui.cli import token

def test_empty_input():

    parsed = token.parse_command("")

    assert parsed is None