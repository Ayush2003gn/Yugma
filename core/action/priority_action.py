import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def priority_action(token_return,task_app):
    if token_return is None:
        logger.error("token_return was None")
        return OperationResult(
            success=False,
            error=ErrorData(
                error_boolean=True,
                error_message="something went wrong",
                error_code="error-no-return-value-from-token"
            )
        )

    if token_return.action == "priority":
        if token_return.task_uid is not None:
            logger.info(f"Updating task with uid {token_return.task_uid}")
            iid_reture = task_app.resolve_uid(token_return.task_uid,token_return.page_name)
            if iid_reture.success is False:

                logger.warning(iid_reture.message)
                return iid_reture
            
        else:
            iid_reture = token_return.task_iid
        
        if token_return.flags.priority is None:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No task name provided for update command",
                    error_code="error-no-task-name-provided-for-update-command"
                )
            )
        
        if token_return.flags.priority.lower() == "low":
            priority_change = task_app.low_priority_task(iid_reture.data,token_return.page_name)
        elif token_return.flags.priority.lower() == "medium":
            priority_change = task_app.medium_priority_task(iid_reture.data,token_return.page_name)
        elif token_return.flags.priority.lower() == "high":
            priority_change = task_app.high_priority_task(iid_reture.data,token_return.page_name)
        else:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No priority provided for update command",
                    error_code="error-no-priority-provided-for-update-command"
                )
            )

        if priority_change.success is False:

            logger.warning(priority_change.message)
            return priority_change

        return priority_change

    elif token_return.action == None:
        logger.error("action was None")
        return OperationResult(
            success=False,
            error=ErrorData(
                error_boolean=True,
                error_message=token_return.error.error_message,
                error_code=token_return.error.error_code
            )
        )