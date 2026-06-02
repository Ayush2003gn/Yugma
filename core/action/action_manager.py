from core.models.taskpage import TaskPage
import logging
from core.action import (
    page_action,
    add_action,
    update_action,
    remove_action,
    priority_action,
    mark_done_action,
    mark_undone_action,
    display_action,
    storage_action
)
logger = logging.getLogger(__name__)

task_app = TaskPage()

def command_paths():
    default = task_app.default

    if default == None:
        return "Yukta/root/-"
    else:
        return f"Yukta/root/{default.category}/-"    

def decision_action(token_return):
    command = token_return.command
    logger.info(f"command: {command}")
    if command == "page":
        logger.info("page command")
        return page_action.page_action(token_return,task_app)
    
    elif command == "add":
        logger.info("add command")
        return add_action.add_action(token_return,task_app)
    
    elif command == "update":
        logger.info("update command")
        return update_action.update_action(token_return,task_app)
    
    elif command == "remove":
        logger.info("remove command")
        return remove_action.remove_action(token_return,task_app)
    
    elif command == "priority":
        logger.info("priority command")
        return priority_action.priority_action(token_return,task_app)
    
    elif command =="mark_done":
        logger.info("mark_done command")
        return mark_done_action.mark_done_action(token_return,task_app)
    
    elif command == "mark_undone":
        logger.info("mark_undone command")
        return mark_undone_action.mark_undone_action(token_return,task_app)
    
    elif command == "display":
        logger.info("display command")
        return display_action.display_action(token_return,task_app)
    
    elif command == "help":
        logger.info("help command")
        return display_action.cmd_exit()
    
    elif command == "exit":
        logger.info("exit command")
        return display_action.cmd_exit()
    
    elif command == None:
        logger.warning("No command provided by user")
        return display_action.cmd_none()
    
    else:
        logger.warning("Invalid command provided by user")
        return display_action.cmd_invalid(token_return)

def action_manager(token_return):
    #return storage_action.storage_action(token_return,task_app)
    pass