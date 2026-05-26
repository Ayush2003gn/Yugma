import logging
import shlex
from core.ui.cli.parser.page_parser import cmd_page
from core.ui.cli.parser.add_parser import cmd_add
from core.ui.cli.parser.remove_parser import cmd_remove
from core.ui.cli.parser.priority__parser import cmd_priority
from core.ui.cli.parser.mark_done_parser import cmd_mark_done
from core.ui.cli.parser.mark_undone_parser import cmd_mark_undone
from core.ui.cli.parser.display_parser import cmd_display, cmd_none, cmd_invalid, cmd_exit, cmd_help  
from core.ui.cli.parser.update_parser import cmd_update
logger = logging.getLogger(__name__)


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
                    logger.info("Exit command received by user")
                    return cmd_exit()

                case None | "":
                    logger.warning("No command from user")
                    return cmd_none()

                case _:
                    logger.error(f"Invalid command received: '{cmd}'")
                    return cmd_invalid(cmd)
