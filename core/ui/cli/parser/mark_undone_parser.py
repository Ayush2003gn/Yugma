from core.contracts.error_data import ErrorData
from core.contracts.command_result import CommandResult
from core.ui.cli.parser.helpers import *
import logging
logger = logging.getLogger(__name__)


def cmd_mark_undone(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="mark_undone",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for mark_undone command", 
                error_code="error-no-task-name"
            )
        )
    task_iid = safe_get_value(argument, "-iid")
    task_uid = safe_get_value(argument, "-uid")
    page = safe_get_value(argument, "--c")

    if "--c" in argument and not page.is_valid:
        logger.warning("No page name provided for mark_undone command")
        return CommandResult(
            command="mark_undone",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for mark_undone command",
                error_code="error-no-page-name"
            )
        )
    
    if not (task_iid.is_valid or task_uid.is_valid):
        logger.warning("No task ID provided for mark_undone command")
        return CommandResult(
            command="mark_done",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for mark_undone command",
                error_code="error-no-task-id"
            )
        )
    elif task_iid.is_valid and task_uid.is_valid:
        return CommandResult(
            command="mark_done",
            error=ErrorData(
                error_boolean=True,
                error_message="both task ID or UID provided for mark_done command",
                error_code="error-no-task-id-or-uid"
            )
        )
    if task_iid.is_valid:
        task_iid = task_iid.value
        task_uid = None
    elif task_uid.is_valid:
        task_uid = task_uid.value
        task_iid = None

    if page.is_valid:
        return CommandResult(
            command="mark_undone",
            action="mark-undone",
            task_iid=task_iid,
            task_uid=task_uid,
            page_name=page.value
        )
    return CommandResult(
        command="mark_undone",
        action="mark-undone",
        task_iid=task_iid,
        task_uid=task_uid,
    )
    