from core.contracts.error_data import ErrorData
from core.contracts.command_result import CommandResult
from core.contracts.date_data import DateData
from core.ui.cli.parser.helpers import *
import logging
logger = logging.getLogger(__name__)

def cmd_display(argument):

    
  
    category = "*"

    # ---------------- CATEGORY ----------------
    page = safe_get_value(argument, "--c")
    if "--c" in argument and page.is_valid:
        category = page.value
        
    elif "--c" in argument and not page.is_valid:
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

def cmd_exit():
    return CommandResult(
        command="exit",
        action="exit"
    )

def cmd_none():
    return CommandResult(
        command="None",
        error=ErrorData(
            error_boolean=True, 
            error_message="No command provided by user", 
            error_code="error-no-command"
        )
    )

def cmd_invalid(cmd):
    return CommandResult(
        command="Invalid",
        error=ErrorData(
            error_boolean=True,
            error_message=f"Invalid command received: '{cmd}'",
            error_code="error-invalid-command"
        )
    )