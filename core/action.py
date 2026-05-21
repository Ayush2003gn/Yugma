from core.models.taskpage import TaskPage
import logging
import core.services.storage as storage
logger = logging.getLogger(__name__)

todo = TaskPage()


def execute_command(token_return):
    if token_return:
        command = token_return.get("command")
        action = token_return.get("action")
        page_name = token_return.get("page_name")
        task_id = token_return.get("task_id")
        task_name = token_return.get("task_name")
        date = token_return.get("date")
        flags = token_return.get("flags")
        logger.info(f"Token return received: Command: {command}, Action: {action}, Page Name: {page_name}, Task ID: {task_id}, Task Name: {task_name}, Date: {date}, Flags: {flags}")

    if command == "page":
        if action == "add":
            add_page_action = add_page(page_name)
            if "default" in flags:
                logger.info(f"page :{page_name} and default flag: {flags['default']}")

                if flags["default"] is True:
                    set_default(page_name)
                    logger.info(f"Page set as default: {page_name}")
            return add_page_action
        
        elif action == "remove":
            return remove_page(page_name)
        elif action == "set_default":
            return set_default(page_name)
        elif action.startswith("error"):
            logger.error(f"Error in page command: {action}")
            return {"success": False, "message": f"Page command error: {action}", "data": None}
        

    elif command == "add":
        if action.startswith("error"):
            logger.error(f"Error in add command: {action}")
            return {"success": False, "message": f"Add command error: {action}", "data": None}
        if "status" in flags:
            logger.info(f"Adding task with status flag: {task_name}, Status: {flags['status']}")

            return add_task(task_name, category=page_name)
        return add_task(task_name, page_name)

    elif command == "remove":
        if action.startswith("error"):
            logger.error(f"Error in remove command: {action}")
            return {"success": False, "message": f"Remove command error: {action}", "data": None}
        return remove_task(task_name, category=page_name)
    
    elif command == "set_priority":
        if action.startswith("error"):
            logger.error(f"Error in set_priority command: {action}")
            return {"success": False, "message": f"Set priority command error: {action}", "data": None}
        priority = flags.get("priority")
        if priority is not None:
            return set_priority(task_name, priority)
        else:
            logger.error("Priority flag missing in set_priority command")
            return {"success": False, "message": "Priority flag missing in set_priority command", "data": None}

    elif command == "mark_done":
        if action.startswith("error"):
            logger.error(f"Error in mark_done command: {action}")
            return {"success": False, "message": f"Mark done command error: {action}", "data": None}
        return mark_done(task_id)
    
    elif command == "mark_undone":
        if action.startswith("error"):
            logger.error(f"Error in mark_undone command: {action}")
            return {"success": False, "message": f"Mark undone command error: {action}", "data": None}
        return mark_undone(task_id)
    
    elif command == "update":
        if action.startswith("error"):
            logger.error(f"Error in update command: {action}")
            return {"success": False, "message": f"Update command error: {action}", "data": None}
        return update_task(task_id, task_name, category=page_name)
    
    elif command == "display":
        if action.startswith("error"):
            logger.error(f"Error in display command: {action}")
            return {"success": False, "message": f"Display command error: {action}", "data": None}
        # Display command is handled in the UI, so we just return success here
        if action == "display-all":
            logger.info(f"Display all command received for category: {page_name}")
            return display_all(category=page_name)
        elif action == "display-done":
            logger.info(f"Display done command received for category: {page_name}")
            return display_done(category=page_name)
        elif action == "display-pending":
            logger.info(f"Display pending command received for category: {page_name}")
            return display_pending(category=page_name)
        elif action == "display-by-day":
            day = flags.get("day")
            month = flags.get("month")
            year = flags.get("year")
            if day is not None and month is not None and year is not None:
                return display_by_day(day, month, year, category=page_name)
            else:
                logger.error("Day, month, or year flag missing in display-by-day command")
                return {"success": False, "message": "Day, month, or year flag missing in display-by-day command", "data": None}
        elif action == "display-by-months":
            month = flags.get("month")
            year = flags.get("year")
            if month is not None and year is not None:
                return display_by_months(month, year, category=page_name)
            else:
                logger.error("Month or year flag missing in display-by-months command")
                return {"success": False, "message": "Month or year flag missing in display-by-months command", "data": None}
        elif action == "display-by-week":
            week = flags.get("week")
            year = flags.get("year")
            if week is not None and year is not None:
                return display_by_week(week, year, category=page_name)
            else:
                logger.error("Week or year flag missing in display-by-week command")
                return {"success": False, "message": "Week or year flag missing in display-by-week command", "data": None}
        elif action == "display-by-year":
            year = flags.get("year")
            if year is not None:
                return display_by_year(year, category=page_name)
            else:
                logger.error("Year flag missing in display-by-year command")
                return {"success": False, "message": "Year flag missing in display-by-year command", "data": None}
    elif command == "display_analysis":
        if action.startswith("error"):
            logger.error(f"Error in display_analysis command: {action}")
            return {"success": False, "message": f"Display analysis command error: {action}", "data": None}
        return display_analysis()
    else:
        logger.error(f"Unknown command: {command}")
        return {"success": False, "message": f"Unknown command: {command}", "data": None}

def command_paths():
    default = todo.default
    if default == None:
        return "Yukta/root/-"
    else:
        return "Yukta/root/"+str(default.category)+"/-"    

def add_page(category):
    return todo.add_page(category)

def remove_page(category):
    return todo.remove_page(category)

def set_default(category):
    logger.info(f"Setting default page: {category} in action module function: set_default")
    return todo.set_default(category)

def add_task(task,category="*"):
    logger.info(f"Adding task: {task}")
    return todo.add_task(task,category)

def remove_task(task,category="*"):
    logger.info(f"Removing task: {task}")
    return todo.remove_task(task,category)

def set_priority(task, priority):
    logger.info(f"Setting priority for task: {task}, Priority: {priority}")
    return todo.set_priority(task, priority)

def mark_done(id):
    logger.info(f"Marking task as done: {id}")
    return todo.mark_done(id)

def mark_undone(id):
    logger.info(f"Marking task as undone: {id}")
    return todo.mark_undone(id)

def update_task(id, task, category="*"):
    logger.info(f"Updating task: {id}, New Task: {task}, Category: {category}")
    return todo.update_task(id, task, category)

def display_all(category="*"):
    logger.info(f"Displaying all tasks for category: {category}")
    return todo.display_all(category)

def display_done(category="*"):
    logger.info(f"Displaying done tasks for category: {category}")
    return todo.display_done(category)

def display_pending(category="*"):
    logger.info(f"Displaying pending tasks for category: {category}")
    return todo.display_pending(category)

def display_by_day(day, months, year, category="*"):
    logger.info(f"Displaying tasks by day: {day}, Months: {months}, Year: {year}, Category: {category}")
    return todo.display_by_day(day, months, year, category)

def display_by_months(months,year, category="*"):
    logger.info(f"Displaying tasks by months: {months}, Year: {year}, Category: {category}")
    return todo.display_by_months(months, year, category)

def display_by_week(week, year, category="*"):
    logger.info(f"Displaying tasks by week: {week}, Year: {year}, Category: {category}")
    return todo.display_by_week(week, year, category)

def display_by_year(year, category="*"):
    logger.info(f"Displaying tasks by year: {year}, Category: {category}")
    return todo.display_by_year(year, category)

def display_analysis():
    logger.info("Displaying analysis")
    return todo.display_analysis()


