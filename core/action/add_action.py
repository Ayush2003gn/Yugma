import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def add_action(token_return,task_app):
    action = token_return.action
    if action == "add-task":

        task_name = token_return.task_name
        page_category = token_return.page_name

        newtask = task_app.add_task(task_name,page_category)
        print("in add action",newtask)
        logger.info(f"{page_category} page:task added [{task_name}]")
        if newtask.success is False:
            logger.warning(newtask.message)
            return newtask

        message_done = ""
        message_priority = ""

        if token_return.flags.status is True:
            markdone = task_app.mark_done(newtask.data.internal_id,page_category)
            
            if markdone.success is False:
                message_done = markdone.error.error_message
        
        if token_return.flags.priority is not None:
            priority = token_return.flags.priority
            if priority == "low":
                priority_change = task_app.low_priority_task(newtask.data.internal_id,page_category)
            elif priority == "medium":
                priority_change = task_app.medium_priority_task(newtask.data.iid,page_category)
            elif priority == "high":
                priority_change = task_app.high_priority_task(newtask.data.internal_id,page_category)

            if priority_change.success is False:
                message_priority = priority_change.error.error_message

        if message_done != "" and message_priority != "":
            logger.warning(f"status:{message_done} priority:{message_priority}")
            return OperationResult(
                success=True, 
                message=f"{newtask.message}", 
                data=newtask.data, 
                error={
                    "error_boolean": True, 
                    "error_message": f"status:{message_done} priority:{message_priority}", 
                    "error_code": "error-change-status-and-priority"
                }
            )
        
        if message_done != "":
            logger.warning(f"status:{message_done}")
            return OperationResult(
                success=True, 
                message=f"{newtask.message}", 
                data=newtask.data, 
                error={
                    "error_boolean": True, 
                    "error_message": f"status:{message_done}", 
                    "error_code": "error-change-status"
                }
            )
        
        if message_priority != "":
            logger.warning(f"priority:{message_priority}")
            return OperationResult(
                success=True, 
                message=f"{newtask.message}", 
                data=newtask.data, 
                error={
                    "error_boolean": True, 
                    "error_message": f"priority:{message_priority}", 
                    "error_code": "error-change-priority"
                }
            )
        
        return OperationResult(
            success=True, 
            message="Task added", 
            data=newtask.data, 
            )
    elif action == None:
        logger.error("action was None")
        return OperationResult(
            success=False,
            error=ErrorData(
                error_boolean=True,
                error_message=token_return.error.error_message,
                error_code=token_return.error.error_code
            )
        )