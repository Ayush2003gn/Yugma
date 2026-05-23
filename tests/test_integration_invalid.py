from core.ui.cli import token

def test_invalid_command():

    parsed = token.parse_command(
        'abcdefg'
    )

    assert parsed is None