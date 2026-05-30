"""from core.ui.cli import token
from core import action

def test_display_flow():

    parsed = token.parse_command(
        'display --all'
    )

    result = action.execute_command(parsed)

    assert result["success"] is True"""