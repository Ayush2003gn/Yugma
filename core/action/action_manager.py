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

def decision_action(token_return):
    command = token_return.command
    
    if command == "page":
        return page_action.page_action(token_return,task_app)
    
    elif command == "add":
        return add_action.add_action(token_return,task_app)
    
    elif command == "update":
        return update_action.update_action(token_return,task_app)
    
    elif command == "remove":
        return remove_action.remove_action(token_return,task_app)
    elif command == "priority":
        return priority_action.priority_action(token_return,task_app)
    elif command =="mark_done":
        return mark_done_action.mark_done_action(token_return,task_app)
    elif command == "mark_undone":
        return mark_undone_action.mark_undone_action(token_return,task_app)
    elif command == "display":
        return display_action.display_action(token_return,task_app)

def action_manager(token_return):
    return storage_action.storage_action(token_return,task_app)