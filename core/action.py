from core.models.taskpage import TaskPage
import logging
logger = logging.getLogger(__name__)
def todo():
    taskpage = TaskPage()
    logger.info("Initializing task page")
    return taskpage

def add_page(category):
    return todo.add_page(category)

def remove_page(category):
    return todo.remove_page(category)

def set_default(category):
    return todo.set_default(category)

def add_task(task,category=None):
    logger.info(f"Adding task: {task}")
    return todo.add_task(task,category)

def remove_task(task,category=None):
    logger.info(f"Removing task: {task}")
    return todo.remove_task(task,category)

def set_priority(task, priority):
    logger.info(f"Setting priority for task: {task}, Priority: {priority}")
    return todo.set_priority(task, priority)

def status(task):
    logger.info(f"Getting status for task: {task}")
    return todo.status(task)

def display(category=None,type_display=None,date=None):
    logger.info(f"Displaying tasks for category: {category}, Type: {type_display}, Date: {date}")
    return todo.display(category,type_display,date)