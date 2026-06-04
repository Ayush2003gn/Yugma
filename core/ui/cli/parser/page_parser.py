from core.contracts.error_data import ErrorData
from core.contracts.command_result import CommandResult
from core.contracts.flags_data import FlagsData
from core.ui.cli.parser.helpers import *
import logging
logger = logging.getLogger(__name__)

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
        default = "--default" in argument
        default_d = "--d" in argument

        if not page_name.is_valid:
            logger.warning("No page name provided for add command")
            return CommandResult(
                command="page",
                error=ErrorData(
                    error_boolean=True, 
                    error_message="No page name provided for add command", 
                    error_code="error-no-page-name"
                )
            )
        if default or default_d:
            return CommandResult(
                command="page",
                action="add",
                page_name=page_name.value,
                    flags=FlagsData(
                        priority=None, 
                        status=None, 
                        default = default or default_d
                    )
            )
        
        return CommandResult(
            command="page",
            action="add",
            page_name=page_name.value,
        )

    if "remove" in argument:
        page_name = safe_get_value(argument, "remove")
        if not page_name.is_valid:
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
            page_name=page_name.value,
        )

    if "set-default" in argument:
        page_name = safe_get_value(argument, "set-default")
        if not page_name.is_valid:
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
            page_name=page_name.value,
            flags=FlagsData(
                priority=None, 
                status=None, 
                default=True
            ),
        )
