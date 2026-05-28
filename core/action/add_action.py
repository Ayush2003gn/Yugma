import logging
from core.contracts.operation_result import OperationResult
from core.contracts.error_data import ErrorData
logger = logging.getLogger(__name__)

def action_add(token_return,task_app):
    action = token_return.action
    if action == "add":

        task_name = token_return.task_name
        page_category = token_return.page_category

        newtask = task_app.add_task(task_name,page_category)
        logger.info(f"{page_category} page:task added [{task_name}]")
        if newtask["success"] is False:
            logger.warning(newtask["message"])
            return ActionResult(
                success=False, 
                message="Can't able to add task", 
                error=ErrorData(
                    error_boolean=True, 
                    error_message=newtask["message"], 
                    error_code="error-add-task"
                )
            )

        message_done = ""
        message_priority = ""

        if token_return.flags.status is True:
            markdone = task_app.mark_done(newtask["data"].internal_id,page_category)
            
            if markdone["success"] is False:
                message_done = markdone["message"]
        
        if token_return.flags.priority is not None:
            priority = token_return.flags.priority
            if priority == "low":
                priority_change = task_app.low_priority_task(newtask["data"].internal_id,page_category)
            elif priority == "medium":
                priority_change = task_app.priority_medium(newtask["data"].internal_id,page_category)
            elif priority == "high":
                priority_change = task_app.high_priority_task(newtask["data"].internal_id,page_category)

            if priority_change["success"] is False:
                message_priority = priority_change["message"]

        if message_done != "" and message_priority != "":
            logger.warning(f"status:{message_done} priority:{message_priority}")
            return ActionResult(
                success=True, 
                message=f"{newtask['message']}", 
                data=newtask["data"], 
                error={
                    "error_boolean": True, 
                    "error_message": f"status:{message_done} priority:{message_priority}", 
                    "error_code": "error-change-status-and-priority"
                }
            )
        
        if message_done != "":
            logger.warning(f"status:{message_done}")
            return ActionResult(
                success=True, 
                message=f"{newtask['message']}", 
                data=newtask["data"], 
                error={
                    "error_boolean": True, 
                    "error_message": f"status:{message_done}", 
                    "error_code": "error-change-status"
                }
            )
        
        if message_priority != "":
            logger.warning(f"priority:{message_priority}")
            return ActionResult(
                success=True, 
                message=f"{newtask['message']}", 
                data=newtask["data"], 
                error={
                    "error_boolean": True, 
                    "error_message": f"priority:{message_priority}", 
                    "error_code": "error-change-priority"
                }
            )
        
        return ActionResult(
            success=True, 
            message="Task added", 
            data=newtask["data"], 
            )