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
        pass
    elif command == "add":
        pass
    elif command == "update":
        pass
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