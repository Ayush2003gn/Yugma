import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def remove_action(token_return,task_app):
    if not token_return:
        logger.error("token_return was None")
        return OperationResult(
            success=False,
            error=ErrorData(
                error_boolean=True,
                error_message="something went wrong",
                error_code="error-no-return-value-from-token"
            )
        )
    
    if token_return.action == "remove-task":
        if token_return.task_uid is not None:
            logger.info(f"Removing task with uid {token_return.task_uid}")
            iid_reture = task_app.resolve_uid(token_return.task_uid,token_return.page_name)
            if iid_reture.success is False:

                logger.warning(iid_reture.message)
                return iid_reture
        else:
            iid_reture = token_return.task_iid

        remove_task = task_app.remove_task(iid_reture.data,token_return.page_name)
            
        if remove_task.success is False:

            logger.warning(remove_task.message)
            return OperationResult(
                success=False,
                error=ErrorData(
                    error_boolean=True,
                    error_message=remove_task.error.error_message,
                    error_code=remove_task.error.error_code
                )
            )

        return remove_task
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
