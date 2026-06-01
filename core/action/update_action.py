import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def update_action(token_return,task_app):
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

    if token_return.action == "update":
        if token_return.task_uid is not None:
            logger.info(f"Updating task with uid {token_return.task_uid}")
            iid_reture = task_app.resolve_uid(token_return.task_uid,token_return.page_name)
            if iid_reture.success is False:

                logger.warning(iid_reture.message)
                return iid_reture
            
        else:
            iid_reture = token_return.task_iid
        
        if token_return.task_name is None:
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message="No task name provided for update command",
                    error_code="error-no-task-name"
                )
            )

        update_task = task_app.update_task(iid = iid_reture.data,task = token_return.task_name,category = token_return.page_name)
        message_done = ""
        message_priority = ""
        if update_task.success is False:

            logger.warning(update_task.message)
            return update_task
        
        if token_return.flags.status is True:
            markdone = task_app.mark_done(iid_reture.data,token_return.page_name)
            
            if markdone.success is False:
                message_done = markdone.error.error_message

        if token_return.flags.priority is not None:
            priority = token_return.flags.priority
            if priority == "low":
                priority_change = task_app.low_priority_task(iid_reture.data,token_return.page_name)
            elif priority == "medium":
                priority_change = task_app.medium_priority_task(iid_reture.data,token_return.page_name)
            elif priority == "high":
                priority_change = task_app.high_priority_task(iid_reture.data,token_return.page_name)

            if priority_change.success is False:
                message_priority = priority_change.error.error_message

        if message_done != "" and message_priority != "":
            logger.warning(f"status:{message_done} priority:{message_priority}")
            return OperationResult(
                success=True,
                message=f"updated task {token_return.task_name}",
                data=None,
                error=ErrorData(
                    error_boolean=True,
                    error_message=f"status:{message_done} priority:{message_priority}",
                    error_code="error-no-return-value-from-token"
                )
            )

        if message_done != "":
            logger.warning(f"status:{message_done}")
            return OperationResult(
                success=True,
                message=f"updated task {token_return.task_name}",
                data=None,
                error=ErrorData(
                    error_boolean=True,
                    error_message=f"status:{message_done}",
                    error_code="error-no-return-value-from-token"
                )
            )

        if message_priority != "":
            logger.warning(f"priority:{message_priority}")
            return OperationResult(
                success=True,
                message=f"updated task {token_return.task_name}",
                data=None,
                error=ErrorData(
                    error_boolean=True,
                    error_message=f"priority:{message_priority}",
                    error_code="error-no-return-value-from-token"
                )
            )

        logger.info(f"updated task {token_return.task_name}")
        return OperationResult(
            success=True,
            message=f"updated task {token_return.task_name}",
            data=None
        )

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