from core.contracts.error_data import ErrorData
from core.contracts.command_result import CommandResult
from core.contracts.flags_data import FlagsData
from core.ui.cli.parser.helpers import *
import logging
logger = logging.getLogger(__name__)


def cmd_update(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="update",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for update command", 
                error_code="error-no-task-name"
            )
        )
    task_id = safe_get_value(argument, "-id")
    task_name = safe_get_value(argument, "-t")
    priority_raw = safe_get_value(argument, "--p")

    priority = validate_priority(priority_raw.value)
    page = safe_get_value(argument, "--c")
    status_flag = None

    if "--md" in argument or "--mark-done" in argument:
        status_flag = "--md"

    elif "--mu" in argument or "--mark-undone" in argument:
        status_flag = "--mu"

    status = validate_status(status_flag)

    if "--c" in argument and not page.is_valid:
        logger.warning("No page name provided for update command")
        return CommandResult(
            command="update",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for update command",
                error_code="error-no-page-name"
            )
        )
    if not task_id.is_valid:
        logger.warning("No task ID provided for update command")
        return CommandResult(
            command="update",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for update command",
                error_code="error-no-task-id"
            )
        )
    if not task_name.is_valid:
        logger.warning("No task name provided for update command")
        return CommandResult(
            command="update",
            error=ErrorData(
                error_boolean=True,
                error_message="No task name provided for update command",
                error_code="error-no-task-name"
            )
        )
    if page.is_valid:
        return CommandResult(
            command="update",
            action="update",
            task_id=task_id.value,
            task_name=task_name.value,
            page_name=page.value,
            flags=FlagsData(priority=priority.value, status=status.value)
        )
    return CommandResult(
        command="update",
        action="update",
        task_id=task_id.value,
        task_name=task_name.value,
        flags=FlagsData(priority=priority.value, status=status.value)
    )
