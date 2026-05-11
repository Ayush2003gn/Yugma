import shlex
import logging
from core.logger import start_up
import core.manager as manager
logger = logging.getLogger(__name__)
Condition = True
manager.import_data()
while Condition:
    try:
        command = input(manager.command_paths() +">>> ")
        parts = shlex.split(command)
        cmd = parts[0]
        argument = parts[1:]
        match cmd.lower():
            case "page" :
                manager.cmd_page(argument)
            
            case "add" | "create":
                manager.cmd_add(argument)

            case "delete" | "remove":
                manager.cmd_remove(argument)

            case "priorty":
                manager.cmd_priorty(argument)
            
            case "status":
                manager.cmd_status(argument)
            
            case "display":
                manager.cmd_display(argument)
            
            case "exit":
                Condition = False

    except KeyboardInterrupt:
        print("Exiting....")
        break

    manager.export_data()