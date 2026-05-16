import logging
import shlex

logger = logging.getLogger(__name__)

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

                case "priorty":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_priorty(argument)
            
                case "status":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_status(argument)
            
                case "display":
                    logger.info(f"command = {cmd} and argument = {argument}")
                    return cmd_display(argument)
            
                case "help":
                    
                    logger.info("Help command received by user")
                    return cmd_help()
            
                case "exit" | "bye":
                    return {"command": "exit",
                            "action": None,
                            "page_name": None,
                            "flags": {"default": False}
                            }
                case None | "":
                    logger.warning("No command from user")
                    return {
                    "command": None,
                    "action": "error-no-command",
                    "page_name": None,
                    "flags": {"default": False}
                    }
                case _:
                    logger.error(f"Invalid command received: '{cmd}'")
                    return {
                    "command": cmd,
                    "action": "error-invalid-command",
                    "page_name": None,
                    "flags": {"default": False}
                    }
                    
            
def cmd_page(argument):
    if len(argument) < 1:
        logger.warning("No page name provided by user")
        return {
            "command": "page",
            "action": "error",
            "page_name": None,
            "flags": {"default": False}
        }
    if "add" in argument:
        index = find_index(argument, "add")
        page_name = argument[index + 1] if index + 1 < len(argument) else None

        if page_name and page_name.startswith("--"):
            page_name = None

        if page_name is None:
            logger.warning("No page name provided for add command")
            return {
                "command": "page",
                "action": "error-no-page-name",
                "page_name": None,
                "flags": {"default": False}
            }
        
        if "--default" in argument:
            return {
                "command": "page",
                "action": "add",
                "page_name": page_name,
                "flags": {"default": True}
            }
        
        return {
            "command": "page",
            "action": "add",
            "page_name": page_name,
            "flags": {"default": False}
        }
    
    if "remove" in argument:
        index = find_index(argument, "remove")
        page_name = argument[index + 1] if index + 1 < len(argument) else None

        if page_name and page_name.startswith("--"):
            page_name = None

        if page_name is None:
            logger.warning("No page name provided for remove command")
            return {
                "command": "page",
                "action": "error-no-page-name",
                "page_name": None,
                "flags": {"default": False}
            }
        
        return {
            "command": "page",
            "action": "remove",
            "page_name": page_name,
            "flags": {"default": False}
        }
    
    if "set-default" in argument:
        index = find_index(argument, "set-default")
        page_name = argument[index + 1] if index + 1 < len(argument) else None
        if page_name and page_name.startswith("--"):
            page_name = None
        if page_name is None:
            logger.warning("No page name provided for set-default command")
            return {
                "command": "page",
                "action": "error-no-page-name",
                "page_name": None,
                "flags": {"default": False}
            }
        return {
            "command": "page",
            "action": "set-default",
            "page_name": page_name,
            "flags": {"default": True}
        }
    
        

def cmd_add(argument):
    pass

def cmd_remove(argument):
    pass

def cmd_priorty(argument):
    pass

def cmd_status(argument):
    pass

def cmd_display(argument):
    pass

def cmd_help(): 
    return {
    "command": "help",
    "action": None,
    "page_name": None,
    "flags": {"default": False}
    }