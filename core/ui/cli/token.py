import logging
import shlex
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)
from typing import Any

@dataclass
class ValidationResult:
    value: Any = None
    is_valid: bool = False
    used_default: bool = False
    error: str | None = None
@dataclass
class ErrorData:
    error_boolean: bool = False
    error_message: str | None = None
    error_code: str | None = None

@dataclass
class FlagsData:
    priority: str | None = None
    status: bool | None = None
    default: bool | None = None

@dataclass
class DateData:
    day: int | None = None
    month: int | None = None
    year: int | None =  None
    week: int | None = None

@dataclass
class CommandResult:
    command: str
    action: str | None = None
    page_name: str | None = None
    task_id: str | None = None
    task_name: str | None = None
    date: DateData = field(
        default_factory=lambda: DateData(None, None, None, None)
    )
    flags: FlagsData = field(
        default_factory=lambda: FlagsData(None, None, None)
    )
    error: ErrorData = field(
        default_factory=lambda: ErrorData(False, None, None)
    )

@dataclass
class DateValidationResult:
    is_valid: bool
    day: int | None = None
    month: int | None = None
    year: int | None =  None
    week: int | None = None
    error: ErrorData = field(
        default_factory=lambda: ErrorData(False, None, None)
    )

def safe_get_value(argument: list, flag: str) -> dict:

    if flag not in argument:
        return {
    "value": None,
    "is_valid": False,
    "error": f"missing-{flag.lstrip('-')}"
}

    index = argument.index(flag)

    if index + 1 >= len(argument):
        return {
    "value": None,
    "is_valid": False,
    "error": "missing-value"
}

    value = argument[index + 1]

    if value.startswith("-"):
        return {
    "value": None,
    "is_valid": False,
    "error": "missing-value"
}

    return {
    "value": value,
    "is_valid": True,
    "error": None
}

def safe_get_date(argument: list, date_type: str) -> dict:

    if date_type == "--year":
        if date_type in argument:
            try:
                year=int(argument[argument.index(date_type) + 1])
            except (ValueError, IndexError):
                return DateValidationResult(
                    is_valid=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"invalid-{date_type.lstrip('-')}",
                        error_code=f"error-invalid-{date_type.lstrip('-')}"
                    )
                )
            return DateValidationResult(
                is_valid=True,
                year=year
            )

    if date_type == "--month":
        if date_type in argument:
            try:
                month=int(argument[argument.index(date_type) + 1])
                year=int(argument[argument.index(date_type) + 2])
            except (ValueError, IndexError):
                return DateValidationResult(
                    is_valid=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"invalid-{date_type.lstrip('-')}",
                        error_code=f"error-invalid-{date_type.lstrip('-')}"
                    )
                )
            return DateValidationResult(
                is_valid=True,
                year=year,
                month=month
            )

    if date_type == "--week":
        if date_type in argument:
            try:
                week=int(argument[argument.index(date_type) + 1])
                year=int(argument[argument.index(date_type) + 2])
            except (ValueError, IndexError):
                return DateValidationResult(
                    is_valid=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"invalid-{date_type.lstrip('-')}",
                        error_code=f"error-invalid-{date_type.lstrip('-')}"
                    )
                )
            return DateValidationResult(
                is_valid=True,
                week=week,
                year=year
            )

    if date_type == "--day":
        if date_type in argument:
            try:
                day=int(argument[argument.index(date_type) + 1])
                month=int(argument[argument.index(date_type) + 2])
                year=int(argument[argument.index(date_type) + 3])
            except (ValueError, IndexError):
                return DateValidationResult(
                    is_valid=False,
                    error=ErrorData(
                        error_boolean=True,
                        error_message=f"invalid-{date_type.lstrip('-')}",
                        error_code=f"error-invalid-{date_type.lstrip('-')}"
                    )
                )
            return DateValidationResult(
                is_valid=True,
                day=day,
                month=month,
                year=year
            )

    return DateValidationResult(
        is_valid=False,
        error=ErrorData(
            error_boolean=True,
            error_message=f"missing-{date_type.lstrip('-')}",
            error_code=f"error-missing-{date_type.lstrip('-')}"
        )
    )


def validate_priority(priority):

    if priority is None:
        return {
            "value": "medium",
            "is_valid": True,
            "used_default": True
        }

    priority = priority.lower()

    if priority not in ["low", "medium", "high"]:
        return {
            "value": "medium",
            "is_valid": False,
            "used_default": True
        }

    return {
        "value": priority,
        "is_valid": True,
        "used_default": False
    }

def validate_status(status):

    if status is None:
        return {
            "value": False,
            "is_valid": True,
            "used_default": True
        }

    if status in ["--md", "--mark-done"]:
        return {
            "value": True,
            "is_valid": True,
            "used_default": False
        }

    if status in ["--mu", "--mark-undone"]:
        return {
            "value": False,
            "is_valid": True,
            "used_default": False
        }

    return {
        "value": False,
        "is_valid": False,
        "used_default": True
    }

def validate_default(default):

    if default is None:
        return {
            "value": False,
            "is_valid": True,
            "used_default": True
        }

    if default in ["--d", "--default"]:
        return {
            "value": True,
            "is_valid": True,
            "used_default": False
        }

    return {
        "value": False,
        "is_valid": False,
        "used_default": True
    }

def parse_command(command):
    parts = shlex.split(command.strip())
    if not parts:
         logger.warning("No command provided by user")
         return None, []
    cmd = parts[0].lower()

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
            
                case "mark-done":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_mark_done(argument)
        
                case "mark-undone":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_mark_undone(argument)
            
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
                    return CommandResult(
                        command=cmd,
                        action="exit",
                    )

                case None | "":
                    logger.warning("No command from user")
                    return CommandResult(
                        command="None",
                        error=ErrorData(
                            error_boolean=True, 
                            error_message="No command provided by user", 
                            error_code="error-no-command"
                        )
                    )

                case _:
                    logger.error(f"Invalid command received: '{cmd}'")
                    return CommandResult(
                        command="Invalid",
                        error=ErrorData(
                            error_boolean=True, 
                            error_message=f"Invalid command received: '{cmd}'"
                            , error_code="error-invalid-command"
                            )
                    )

#-----------------page command handler-----------------            
def cmd_page(argument):
    if len(argument) < 1:
        logger.warning("No page name provided by user")
        return CommandResult(
            command="page",
            error=ErrorData(
                error_boolean=True, 
                error_message="No page name provided by user", 
                error_code="error-no-page-name"
            )
        )
    
    if "add" in argument:
        page_name = safe_get_value(argument, "add")
        default_raw = safe_get_value(argument, "--default")
        default = validate_default(default_raw["value"])
        default_d_raw = safe_get_value(argument, "--d")
        default_d = validate_default(default_d_raw["value"])

        if not page_name["is_valid"]:
            logger.warning("No page name provided for add command")
            return CommandResult(
                command="page",
                error=ErrorData(
                    error_boolean=True, 
                    error_message="No page name provided for add command", 
                    error_code="error-no-page-name"
                )
            )
        
        if default["value"] or default_d["value"]:
            return CommandResult(
                command="page",
                action="add",
                page_name=page_name["value"],
                flags=FlagsData(
                    priority=None, 
                    status=None, 
                    default=default["value"]
                )
            )
        
        return CommandResult(
            command="page",
            action="add",
            page_name=page_name["value"],
        )

    if "remove" in argument:
        page_name = safe_get_value(argument, "remove")
        if not page_name["is_valid"]:
            logger.warning("No page name provided for remove command")
            return CommandResult(
                command="page",
                error=ErrorData(
                    error_boolean=True,
                    error_message="No page name provided for remove command",
                    error_code="error-no-page-name"
                )
            )
        return CommandResult(
            command="page",
            action="remove",
            page_name=page_name["value"],
        )

    if "set-default" in argument:
        page_name = safe_get_value(argument, "set-default")
        if not page_name["is_valid"]:
            logger.warning("No page name provided for set-default command")
            return CommandResult(
                command="page",
                error=ErrorData(
                    error_boolean=True,
                    error_message="No page name provided for set-default command",
                    error_code="error-no-page-name"
                )
            )
        return CommandResult(
            command="page",
            action="set-default",
            page_name=page_name["value"],
            flags=FlagsData(
                priority=None, 
                status=None, 
                default=True
            ),
        )

#-----------------task in page command handler-----------------
def cmd_add(argument):#i/p add -t "task name" (option --c "page category name" or use default page)
    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="add",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for add command", 
                error_code="error-no-task-name")
        )

    task = safe_get_value(argument, "-t")
    page = safe_get_value(argument, "--c")
    priority_raw = safe_get_value(argument, "--p")

    priority = validate_priority(priority_raw["value"])
    status_flag = None

    if "--md" in argument or "--mark-done" in argument:
        status_flag = "--md"

    elif "--mu" in argument or "--mark-undone" in argument:
        status_flag = "--mu"

    status = validate_status(status_flag)

    if not task["is_valid"]:
        logger.warning("No task name provided for add command")
        return CommandResult(
            command="add",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for add command", 
                error_code="error-no-task-name"
                )
        )

    if "--c" in argument and not page["is_valid"]:
        logger.warning("No page name provided for add command, using default page")
        return CommandResult(
            command="add",
            action="add-task",
            task_name=task["value"],
            flags=FlagsData(
                priority=priority["value"],
                status=status["value"]
            ),
            error=ErrorData(
                error_boolean=True, 
                error_message="No page name provided for add command, using default page", 
                error_code="error-no-page-name"
                )
        )

    if not page["is_valid"]:
        logger.info("No page name provided for add command, using default page")
        return CommandResult(
            command="add",
            action="add-task",
            task_name=task["value"],
            flags=FlagsData(priority=priority["value"], status=status["value"])
        )

    return CommandResult(
        command="add",
        action="add-task",
        page_name=page["value"],
        task_name=task["value"],
        flags=FlagsData(priority=priority["value"], status=status["value"])
    )

def cmd_remove(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="remove",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for remove command", 
                error_code="error-no-task-name"
            )
        ) 
    
    task_id = safe_get_value(argument, "-id")
    page = safe_get_value(argument, "--c")

    if "--c" in argument and not page["is_valid"]:
        logger.warning("No page name provided for remove command")
        return CommandResult(
            command="remove",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for remove command",
                error_code="error-no-page-name"
            )
        )
    
    if not task_id["is_valid"]:
        logger.warning("No task ID provided for remove command")
        return CommandResult(
            command="remove",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for remove command",
                error_code="error-no-task-id"
            )
        )

    if page["is_valid"]:
        return CommandResult(
            command="remove",
            action="remove-task",
            task_id=task_id["value"],
            page_name=page["value"]
        )

    return CommandResult(
        command="remove",
        action="remove-task",
        task_id=task_id["value"]
    )


def cmd_priority(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="priority",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for priority command", 
                error_code="error-no-task-name"
            )
        )

    task_id = safe_get_value(argument, "-id")
    priority_raw = safe_get_value(argument, "--p")

    priority = validate_priority(priority_raw["value"])
    page = safe_get_value(argument, "--c")

    if "--c" in argument and not page["is_valid"]:
        logger.warning("No page name provided for priority command")
        return CommandResult(
            command="priority",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for priority command",
                error_code="error-no-page-name"
            )
        )
    if not priority["is_valid"]:
        logger.warning("No priority provided for priority command")
        return CommandResult(
            command="priority",
            error=ErrorData(
                error_boolean=True,
                error_message="No priority provided for priority command",
                error_code="error-no-priority"
            )
        )
    
    if not task_id["is_valid"]:
        logger.warning("No task ID provided for priority command")
        return CommandResult(
            command="priority",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for priority command",
                error_code="error-no-task-id"
            )
        )
    if page["is_valid"]:
        return CommandResult(
            command="priority",
            action="set-priority",
            task_id=task_id["value"],
            page_name=page["value"],
            flags=FlagsData(priority=priority["value"])
        )
    return CommandResult(
        command="priority",
        action="set-priority",
        task_id=task_id["value"],
        flags=FlagsData(priority=priority["value"])
    )

def cmd_mark_done(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="mark_done",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for mark_done command", 
                error_code="error-no-task-name"
            )
        )
    task_id = safe_get_value(argument, "-id")
    page = safe_get_value(argument, "--c")

    if "--c" in argument and not page["is_valid"]:
        logger.warning("No page name provided for mark_done command")
        return CommandResult(
            command="mark_done",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for mark_done command",
                error_code="error-no-page-name"
            )
        )
    if not task_id["is_valid"]:
        logger.warning("No task ID provided for mark_done command")
        return CommandResult(
            command="mark_done",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for mark_done command",
                error_code="error-no-task-id"
            )
        )
    if page["is_valid"]:
        return CommandResult(
            command="mark_done",
            action="mark-done",
            task_id=task_id["value"],
            page_name=page["value"]
        )
    return CommandResult(
        command="mark_done",
        action="mark-done",
        task_id=task_id["value"]
    )

def cmd_mark_undone(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="mark_undone",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for mark_undone command", 
                error_code="error-no-task-name"
            )
        )
    task_id = safe_get_value(argument, "-id")
    page = safe_get_value(argument, "--c")

    if "--c" in argument and not page["is_valid"]:
        logger.warning("No page name provided for mark_undone command")
        return CommandResult(
            command="mark_undone",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for mark_undone command",
                error_code="error-no-page-name"
            )
        )
    if not task_id["is_valid"]:
        logger.warning("No task ID provided for mark_undone command")
        return CommandResult(
            command="mark_undone",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for mark_undone command",
                error_code="error-no-task-id"
            )
        )
    if page["is_valid"]:
        return CommandResult(
            command="mark_undone",
            action="mark-undone",
            task_id=task_id["value"],
            page_name=page["value"]
        )
    return CommandResult(
        command="mark_undone",
        action="mark-undone",
        task_id=task_id["value"]
    )
    
def cmd_update(argument):

    if len(argument) < 1:
        logger.warning("No task name provided by user")
        return CommandResult(
            command="update",
            error=ErrorData(
                error_boolean=True, 
                error_message="No task name provided for update command", 
                error_code="error-no-task-name"
            )
        )
    task_id = safe_get_value(argument, "-id")
    task_name = safe_get_value(argument, "-t")
    priority_raw = safe_get_value(argument, "--p")

    priority = validate_priority(priority_raw["value"])
    page = safe_get_value(argument, "--c")
    status_flag = None

    if "--md" in argument or "--mark-done" in argument:
        status_flag = "--md"

    elif "--mu" in argument or "--mark-undone" in argument:
        status_flag = "--mu"

    status = validate_status(status_flag)

    if "--c" in argument and not page["is_valid"]:
        logger.warning("No page name provided for update command")
        return CommandResult(
            command="update",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for update command",
                error_code="error-no-page-name"
            )
        )
    if not task_id["is_valid"]:
        logger.warning("No task ID provided for update command")
        return CommandResult(
            command="update",
            error=ErrorData(
                error_boolean=True,
                error_message="No task ID provided for update command",
                error_code="error-no-task-id"
            )
        )
    if not task_name["is_valid"]:
        logger.warning("No task name provided for update command")
        return CommandResult(
            command="update",
            error=ErrorData(
                error_boolean=True,
                error_message="No task name provided for update command",
                error_code="error-no-task-name"
            )
        )
    if page["is_valid"]:
        return CommandResult(
            command="update",
            action="update",
            task_id=task_id["value"],
            task_name=task_name["value"],
            page_name=page["value"],
            flags=FlagsData(priority=priority["value"], status=status["value"])
        )
    return CommandResult(
        command="update",
        action="update",
        task_id=task_id["value"],
        task_name=task_name["value"],
        flags=FlagsData(priority=priority["value"], status=status["value"])
    )

def cmd_display(argument):

    
  
    category = "*"

    # ---------------- CATEGORY ----------------
    page = safe_get_value(argument, "--c")
    if "--c" in argument and page["is_valid"]:
        category = page["value"]
        
    elif "--c" in argument and not page["is_valid"]:
        logger.warning("No page name provided for display command")
        return CommandResult(
            command="display",
            error=ErrorData(
                error_boolean=True,
                error_message="No page name provided for display command",
                error_code="error-no-page-name"
            )
        )
    # ---------------- ALL TASKS ----------------
    if not argument:
        logger.info("Displaying all tasks")
        return CommandResult(
            command="display",
            action="display-all",
            page_name=category
        )
    
    elif "--all" in argument:
        logger.info(f"Displaying all tasks in category: {category}")
        return CommandResult(
            command="display",
            action="display-all",
            page_name=category
        )

    # ---------------- ANALYSIS ----------------
    elif "--analysis" in argument or "--A" in argument:
        logger.info("Displaying analysis")
        return CommandResult(
            command="display",
            action="display-analysis"
        )
    
    # ---------------- YEAR ----------------
    elif "--year" in argument:
         date_val = safe_get_date(argument, "--year")
         if date_val.is_valid:
            return CommandResult(
                command="display",
                action="display-by-year",
                page_name=category,
                date=DateData(year=date_val.year)
            )
         return CommandResult(
            command="display",
            error=ErrorData(
                error_boolean=True,
                error_message=date_val.error.error_message,
                error_code=date_val.error.error_code
            )
         )
    # ---------------- MONTH ----------------
    elif "--month" in argument:
        date_val = safe_get_date(argument, "--month")
        if date_val.is_valid:
            return CommandResult(
                command="display",
                action="display-by-month",
                page_name=category,
                date=DateData(month=date_val.month, year=date_val.year)
            )
        return CommandResult(
            command="display",
            error=ErrorData(
                error_boolean=True,
                error_message=date_val.error.error_message,
                error_code=date_val.error.error_code
            )
         )
        
    # ---------------- WEEK ----------------
    elif "--week" in argument:
        date_val = safe_get_date(argument, "--week")
        if date_val.is_valid:
            return CommandResult(
                command="display",
                action="display-by-week",
                page_name=category,
                date=DateData(week=date_val.week, year=date_val.year)
            )
        return CommandResult(
            command="display",
            error=ErrorData(
                error_boolean=True,
                error_message=date_val.error.error_message,
                error_code=date_val.error.error_code
            )
         )
    # ---------------- DAY ----------------
    elif "--day" in argument:
        date_val = safe_get_date(argument, "--day")
        if date_val.is_valid:
            return CommandResult(
                command="display",
                page_name=category,
                action="display-by-day",
                date=DateData(day=date_val.day, month=date_val.month, year=date_val.year)
            )
        return CommandResult(
            command="display",
            error=ErrorData(
                error_boolean=True,
                error_message=date_val.error.error_message,
                error_code=date_val.error.error_code
            )
         )
    else:
        logger.warning("No date provided for display command")
        return CommandResult(
            command="display",
            error=ErrorData(
                error_boolean=True,
                error_message="No date provided for display command",
                error_code="error-no-date"
            )
        )
def cmd_help():
    return CommandResult(
        command="help",
        action="help"
    )