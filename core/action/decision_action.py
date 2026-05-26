from core.models.taskpage import TaskPage
import logging
import core.action.handle_page_command as handle_page_command
import core.action.handle_add_command as handle_add_command
import core.action.handle_update_command as handle_update_command
logger = logging.getLogger(__name__)

todo = TaskPage()

def decision_action(token_return, todo):
    if token_return and isinstance(token_return, dict):
        command = token_return.get("command")
        action = token_return.get("action")
        page_name = token_return.get("page_name")
        task_id = token_return.get("task_id")
        task_name = token_return.get("task_name")
        date = token_return.get("date")
        flags = token_return.get("flags")
        logger.info(f"Token return received: Command: {command}, Action: {action}, Page Name: {page_name}, Task ID: {task_id}, Task Name: {task_name}, Date: {date}, Flags: {flags}")
    
    else:
        logger.warning("No token return received")
        return {"success": False, "message": "No token return received", "data": None}
    
    if command == "page":
        return handle_page_command(action, page_name)
    elif command == "add":
        return handle_add_command(action, task_name, date, flags)
    elif command == "update":
        return handle_update_command(action, task_id, task_name, date, flags)
    elif command == "remove":
        pass
    elif command == "priority":
        pass
    elif command =="mark_done":
        pass
    elif command == "mark_undone":
        pass
    elif command == "display":
        pass