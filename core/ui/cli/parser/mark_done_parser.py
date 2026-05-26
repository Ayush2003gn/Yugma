from core.contracts.error_data import ErrorData
from core.contracts.command_result import CommandResult
from core.contracts.date_data import DateData
from core.contracts.flags_data import FlagsData
from core.ui.cli.parser.helpers import *
import logging
logger = logging.getLogger(__name__)

def cmd_mark_done(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="mark_done",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for mark_done command", 
                error_code="error-no-task-name"
            )
        )
    task_id = safe_get_value(argument, "-id")
    page = safe_get_value(argument, "--c")

    if "--c" in argument and not page.is_valid:
        logger.warning("No page name provided for mark_done command")
        return CommandResult(
            command="mark_done",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for mark_done command",
                error_code="error-no-page-name"
            )
        )
    if not task_id.is_valid:
        logger.warning("No task ID provided for mark_done command")
        return CommandResult(
            command="mark_done",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for mark_done command",
                error_code="error-no-task-id"
            )
        )
    if page.is_valid:
        return CommandResult(
            command="mark_done",
            action="mark-done",
            task_id=task_id.value,
            page_name=page.value
        )
    return CommandResult(
        command="mark_done",
        action="mark-done",
        task_id=task_id.value
    )
