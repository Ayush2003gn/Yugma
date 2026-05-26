from core.contracts.error_data import ErrorData
from core.contracts.command_result import CommandResult
from core.contracts.flags_data import FlagsData
from core.ui.cli.parser.helpers import *
import logging
logger = logging.getLogger(__name__)

def cmd_priority(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="priority",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for priority command", 
                error_code="error-no-task-name"
            )
        )

    task_id = safe_get_value(argument, "-id")
    priority_raw = safe_get_value(argument, "--p")

    priority = validate_priority(priority_raw.value)
    page = safe_get_value(argument, "--c")

    if "--c" in argument and not page.is_valid:
        logger.warning("No page name provided for priority command")
        return CommandResult(
            command="priority",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for priority command",
                error_code="error-no-page-name"
            )
        )
    if not priority.is_valid:
        logger.warning("No priority provided for priority command")
        return CommandResult(
            command="priority",
            error=ErrorData(
                error_boolean=True,
                error_message="No priority provided for priority command",
                error_code="error-no-priority"
            )
        )
    
    if not task_id.is_valid:
        logger.warning("No task ID provided for priority command")
        return CommandResult(
            command="priority",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for priority command",
                error_code="error-no-task-id"
            )
        )
    if page.is_valid:
        return CommandResult(
            command="priority",
            action="set-priority",
            task_id=task_id.value,
            page_name=page.value,
            flags=FlagsData(priority=priority.value)
        )
    return CommandResult(
        command="priority",
        action="set-priority",
        task_id=task_id.value,
        flags=FlagsData(priority=priority.value)
    )
