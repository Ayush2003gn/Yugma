from core.contracts.error_data import ErrorData
from core.contracts.command_result import CommandResult
from core.contracts.date_data import DateData
from core.contracts.flags_data import FlagsData
from core.ui.cli.parser.helpers import *
import logging
logger = logging.getLogger(__name__)

def cmd_add(argument):#i/p add -t "task name" (option --c "page category name" or use default page)
    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="add",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for add command", 
                error_code="error-no-task-name")
        )

    task = safe_get_value(argument, "-t")
    page = safe_get_value(argument, "--c")
    priority_raw = safe_get_value(argument, "--p")

    priority = validate_priority(priority_raw.value)
    status_flag = None

    if "--md" in argument or "--mark-done" in argument:
        status_flag = "--md"

    elif "--mu" in argument or "--mark-undone" in argument:
        status_flag = "--mu"

    status = validate_status(status_flag)

    if not task.is_valid:
        logger.warning("No task name provided for add command")
        return CommandResult(
            command="add",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for add command", 
                error_code="error-no-task-name"
                )
        )

    if "--c" in argument and not page.is_valid:
        logger.warning("No page name provided for add command, using default page")
        return CommandResult(
            command="add",
            action="add-task",
            task_name=task.value,
            flags=FlagsData(
                priority=priority.value,
                status=status.value
            ),
            error=ErrorData(
                error_boolean=True, 
                error_message="No page name provided for add command, using default page", 
                error_code="error-no-page-name"
                )
        )

    if not page.is_valid:
        logger.info("No page name provided for add command, using default page")
        return CommandResult(
            command="add",
            action="add-task",
            task_name=task.value,
            flags=FlagsData(priority=priority.value, status=status.value)
        )

    return CommandResult(
        command="add",
        action="add-task",
        page_name=page.value,
        task_name=task.value,
        flags=FlagsData(priority=priority.value, status=status.value)
    )
