import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def mark_undone_action(token_return,task_app):
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

    if token_return.action == "mark-undone":
        if token_return.task_uid is not None:
            logger.info(f"Updating task with uid {token_return.task_uid}")
            iid_reture = task_app.resolve_uid(token_return.task_uid,token_return.page_name)
            if iid_reture.success is False:

                logger.warning(iid_reture.message)
                return iid_reture
            
        else:
            iid_reture = token_return.task_iid

        mark_undone = task_app.mark_undone(iid_reture.data,token_return.page_name)

        if mark_undone.success is False:

            logger.warning(mark_undone.message)
            return mark_undone

        return mark_undone
    elif token_return.action == None:
        return OperationResult(
            success=False, 
            error=ErrorData(
                error_boolean=True, 
                error_message="No action provided", 
                error_code="error-no-action-provided"
            )
        )