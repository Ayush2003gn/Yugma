import logging
import shlex

logger = logging.getLogger(__name__)

def uniform_return(command, action, page_name=None, task_id=None, task_name=None, date=None, flags=None):
    """Helper function to create uniform return structure"""
    if flags is None:
        flags = {}
    if date is None:
        date = {"day": None, "month": None, "year": None}
    
    return {
        "command": command,
        "action": action,
        "page_name": page_name,
        "task_id": task_id,
        "task_name": task_name,
        "date": date,
        "flags": flags
    }

def find_index(lst, value):
    for i, item in enumerate(lst):
        if item == value:
            return i
    return None

def command_breakdown(command):
    parts = shlex.split(command.strip().lower())
    if not parts:
         return None, []
    cmd = parts[0]
    if cmd is None:
        logger.warning("No command provided by user")
        return None, []
    cmd = cmd.lower()
    argument = parts[1:]
    return cmd, argument

def command_handler(cmd, argument):
    match cmd:
                case "page" :
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_page(argument)
            
                case "add" | "create":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_add(argument)

                case "delete" | "remove":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_remove(argument)

                case "priority":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_priority(argument)
            
                case "status":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_status(argument)
            
                case "display":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_display(argument)

                case "update":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_update(argument)
            
                case "help":
                    
                    logger.info("Help command received by user")
                    return cmd_help()
            
                case "exit" | "bye":
                    return uniform_return("exit", None, flags={"default": False})
                case None | "":
                    logger.warning("No command from user")
                    return uniform_return(None, "error-no-command", flags={"default": False})
                case _:
                    logger.error(f"Invalid command received: '{cmd}'")
                    return uniform_return(cmd, "error-invalid-command", flags={"default": False})
                    
#-----------------page command handler-----------------            
def cmd_page(argument):
    if len(argument) < 1:
        logger.warning("No page name provided by user")
        return uniform_return("page", "error", flags={"default": False})
    if "add" in argument:
        index = find_index(argument, "add")
        page_name = argument[index + 1] if index + 1 < len(argument) else None

        if page_name and (page_name.startswith("--") or page_name.startswith("-")):
            page_name = None

        if page_name is None:
            logger.warning("No page name provided for add command")
            return uniform_return("page", "error-no-page-name", flags={"default": False})
        
        if "--default" in argument:
            return uniform_return("page", "add", page_name=page_name, flags={"default": True})
        
        return uniform_return("page", "add", page_name=page_name, flags={"default": False})
    
    if "remove" in argument:
        index = find_index(argument, "remove")
        page_name = argument[index + 1] if index + 1 < len(argument) else None

        if page_name and (page_name.startswith("--") or page_name.startswith("-")):
            page_name = None

        if page_name is None:
            logger.warning("No page name provided for remove command")
            return uniform_return("page", "error-no-page-name", flags={"default": False})
        
        return uniform_return("page", "remove", page_name=page_name, flags={"default": False})
    
    if "set-default" in argument:
        index = find_index(argument, "set-default")
        page_name = argument[index + 1] if index + 1 < len(argument) else None
        if page_name and (page_name.startswith("--") or page_name.startswith("-")):
            page_name = None
        if page_name is None:
            logger.warning("No page name provided for set-default command")
            return uniform_return("page", "error-no-page-name", flags={"default": False})
        return uniform_return("page", "set-default", page_name=page_name, flags={"default": True})
    
        
#-----------------task in page command handler-----------------
def cmd_add(argument):#i/p add -t "task name" (option --c "page category name" or use default page)
    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return uniform_return("add", "error-no-task-name", flags={"priority": None, "status": False})

    if "-t" in argument:
        
        index = find_index(argument, "-t")
        task_name = argument[index + 1] if index + 1 < len(argument) else None

        if task_name and (task_name.startswith("--") or task_name.startswith("-")):
            task_name = None

        if task_name is None:
            logger.warning("No task name provided for add command")
            return uniform_return("add", "error-no-task-name", flags={"priority": None, "status": False})

        action = "add-task"
        page_name = None
        if "--c" in argument:
            index = find_index(argument, "--c")
            page_name = argument[index + 1] if index + 1 < len(argument) else None

            if page_name and (page_name.startswith("--") or page_name.startswith("-")):
                page_name = None
                logger.warning("No page name provided for add command")
                return uniform_return("add", "error-no-page-name", flags={"priority": None, "status": False})

            if page_name is None:
                logger.warning("No page name provided for add command, using default page")
        else:
            logger.info("No page name provided for add command, using default page")

        priority = None
        if "--p" in argument:
            index = find_index(argument, "--p")
            priority = argument[index + 1] if index + 1 < len(argument) else None
            if priority and (priority.startswith("--") or priority.startswith("-")):
                priority = "Normal"
            elif priority not in ["low", "normal", "high"]:
                logger.warning("Invalid priority value provided for add command")
                priority = "Normal"
        
        status = False
        if "--md" in argument:
            status = True
        
        return uniform_return("add", action, page_name=page_name, task_name=task_name, flags={"priority": priority, "status": status})
    
    return uniform_return("add", None, flags={"priority": None, "status": False})

def cmd_remove(argument):
    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return uniform_return("remove", "error-no-task-id", flags={"priority": None, "status": False})
    if "-id" in argument:
        index = find_index(argument, "-id")
        task_id = argument[index + 1] if index + 1 < len(argument) else None

        if task_id and (task_id.startswith("--") or task_id.startswith("-")):
            task_id = None

        if task_id is None:
            logger.warning("No task ID provided for remove command")
            return uniform_return("remove", "error-no-task-id", flags={"priority": None, "status": False})
        
        return uniform_return("remove", "remove-task", task_id=task_id, flags={"priority": None, "status": False})
    
    return uniform_return("remove", "error-no-task-id", flags={"priority": None, "status": False})

def cmd_priority(argument):
    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return uniform_return("priority", "error-no-task-id", flags={"priority": None, "status": False})
    if "-id" in argument and "--p" in argument:
        index_id = find_index(argument, "-id")
        task_id = argument[index_id + 1] if index_id + 1 < len(argument) else None

        if task_id and (task_id.startswith("--") or task_id.startswith("-")):
            task_id = None

        if task_id is None:
            logger.warning("No task ID provided for priority command")
            return uniform_return("priority", "error-no-task-id", flags={"priority": None, "status": False})
        
        index_p = find_index(argument, "--p")
        priority = argument[index_p + 1] if index_p + 1 < len(argument) else None

        if priority and (priority.startswith("--") or priority.startswith("-")):
            priority = None

        if priority is None:
            logger.warning("No priority value provided for priority command")
            return uniform_return("priority", "error-no-priority-value", flags={"priority": None, "status": False})
        if priority not in ["low", "normal", "high"]:
            logger.warning("Invalid priority value provided for priority command")
            return uniform_return("priority", "error-invalid-priority-value", flags={"priority": None, "status": False})
        return uniform_return("priority", "set-priority", task_id=task_id, flags={"priority": priority, "status": False})
    
    return uniform_return("priority", "error-no-task-id", flags={"priority": None, "status": False})

def cmd_status(argument):
    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return uniform_return("status", "error-no-task-id", flags={"priority": None, "status": False})
    if "-id" in argument:
        index = find_index(argument, "-id")
        task_id = argument[index + 1] if index + 1 < len(argument) else None

        if task_id and (task_id.startswith("--") or task_id.startswith("-")):
            task_id = None

        if task_id is None:
            logger.warning("No task ID provided for status command")
            return uniform_return("status", "error-no-task-id", flags={"priority": None, "status": False})
        if "--md" in argument:
            status = True
        elif "--mu" in argument:
            status = False
        else:
            logger.warning("No status value provided for status command")
            return uniform_return("status", "error-no-status-value", flags={"priority": None, "status": False})
        
        return uniform_return("status", "toggle-status", task_id=task_id, flags={"priority": None, "status": status})
    
    return uniform_return("status", "error-no-task-id", flags={"priority": None, "status": False})

def cmd_update(argument):
    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return uniform_return("update", "error-no-task-id", flags={"priority": None, "status": False})
    if "-id" in argument:
        index = find_index(argument, "-id")
        task_id = argument[index + 1] if index + 1 < len(argument) else None

        if task_id and (task_id.startswith("--") or task_id.startswith("-")):
            task_id = None

        if task_id is None:
            logger.warning("No task ID provided for update command")
            return uniform_return("update", "error-no-task-id", flags={"priority": None, "status": False})
        
        new_name = None
        if "-t" in argument:
            index = find_index(argument, "-t")
            new_name = argument[index + 1] if index + 1 < len(argument) else None

            if new_name and (new_name.startswith("--") or new_name.startswith("-")):
                new_name = None

        priority = None
        if "--p" in argument:
            index = find_index(argument, "--p")
            priority = argument[index + 1] if index + 1 < len(argument) else None
            if priority and (priority.startswith("--") or priority.startswith("-")):
                priority = "Normal"
            elif priority not in ["low", "normal", "high"]:
                logger.warning("Invalid priority value provided for update command")
                priority = "Normal"
        
        status = None
        if "--md" in argument:
            status = True
        elif "--mu" in argument:
            status = False
        
        return uniform_return("update", "update-task", task_id=task_id, task_name=new_name, flags={"priority": priority, "status": status})
    
    return uniform_return("update", "error-no-task-id", flags={"priority": None, "status": False})

def cmd_display(argument):
    
    # ---------------- DEFAULT ----------------
    if not argument:
        logger.info("Displaying all tasks")
        return uniform_return("display", "display-all", flags={"default": False})

    category = "*"

    # ---------------- CATEGORY ----------------
    if "--c" in argument:
        index = find_index(argument, "--c")
        if index + 1 < len(argument):
            category = argument[index + 1]

    # ---------------- ALL TASKS ----------------
    if "--all" in argument:
        logger.info(f"Displaying all tasks in category: {category}")
        return uniform_return("display", "display-all", page_name=category, flags={"default": False})

    # ---------------- ANALYSIS ----------------
    elif "--analysis" in argument or "--A" in argument:
        logger.info("Displaying analysis")
        return uniform_return("display", "display-analysis", flags={"default": False})

    # ---------------- YEAR ----------------
    elif "--year" in argument:
        index = find_index(argument, "--year")

        if index + 1 >= len(argument):
            logger.warning("Year missing")
            return uniform_return("display", "error-year-missing", date={"day": None, "month": None, "year": None})
        try:
            year = int(argument[index + 1])
        except ValueError:
            logger.warning("Invalid year value")
            return uniform_return("display", "error-invalid-year", date={"day": None, "month": None, "year": None})

        return uniform_return("display", "display-by-year", date={"day": None, "month": None, "year": year})

    # ---------------- MONTH ----------------
    elif "--month" in argument:
        index = find_index(argument, "--month")

        if index + 2 >= len(argument):
            logger.warning("Month or Year missing")
            return uniform_return("display", "error-month-year-missing", date={"day": None, "month": None, "year": None})
        try:
            month = argument[index + 1]
            year = int(argument[index + 2])
        except ValueError:
            logger.warning("Invalid month or year value")
            return uniform_return("display", "error-invalid-month-year", date={"day": None, "month": None, "year": None})

        return uniform_return("display", "display-by-month", date={"day": None, "month": month, "year": year})

    # ---------------- WEEK ----------------
    elif "--week" in argument:
        index = find_index(argument, "--week")

        if index + 2 >= len(argument):
            logger.warning("Week or Year missing")
            return uniform_return("display", "error-week-year-missing", date={"day": None, "month": None, "year": None})
        try:
            week = int(argument[index + 1])
            year = int(argument[index + 2])
        except ValueError:
            logger.warning("Invalid week or year value")
            return uniform_return("display", "error-invalid-week-year", date={"day": None, "month": None, "year": None})

        return uniform_return("display", "display-by-week", date={"day": week, "month": None, "year": year})

    # ---------------- DAY ----------------
    elif "--day" in argument:
        index = find_index(argument, "--day")

        if index + 3 >= len(argument):
            logger.warning("Day Month Year missing")
            return uniform_return("display", "error-day-month-year-missing", date={"day": None, "month": None, "year": None})
        try:
            day = int(argument[index + 1])
            month = int(argument[index + 2])
            year = int(argument[index + 3])
        except ValueError:
            logger.warning("Invalid day, month, or year value")
            return uniform_return("display", "error-invalid-day-month-year", date={"day": None, "month": None, "year": None})

        return uniform_return("display", "display-by-day", date={"day": day, "month": month, "year": year})

    else:
        logger.error("Unknown display command")
        return uniform_return("display", "error-unknown-command", date={"day": None, "month": None, "year": None})

def cmd_help():
    return uniform_return("help", "display-help", flags={"default": False})