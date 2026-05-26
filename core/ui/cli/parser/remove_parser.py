from core.contracts.error_data import ErrorData
from core.contracts.command_result import CommandResult
from core.ui.cli.parser.helpers import *
import logging
logger = logging.getLogger(__name__)

def cmd_remove(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="remove",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for remove command", 
                error_code="error-no-task-name"
            )
        ) 
    

    task_id = safe_get_value(argument, "-id")
    page = safe_get_value(argument, "--c")

    if "--c" in argument and not page.is_valid:
        logger.warning("No page name provided for remove command")
        return CommandResult(
            command="remove",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for remove command",
                error_code="error-no-page-name"
            )
        )
    
    if not task_id.is_valid:
        logger.warning("No task ID provided for remove command")
        return CommandResult(
            command="remove",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for remove command",
                error_code="error-no-task-id"
            )
        )

    if page.is_valid:
        return CommandResult(
            command="remove",
            action="remove-task",
            task_id=task_id.value,
            page_name=page.value
        )

    return CommandResult(
        command="remove",
        action="remove-task",
        task_id=task_id.value
    )
