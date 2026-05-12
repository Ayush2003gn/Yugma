import shlex
import logging
import core.logger
import core.manager as manager
core.logger.start_up()
logger = logging.getLogger(__name__)

logger.info("Program started")

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
                logger.info(f"command = {cmd} and argument = {argument}")
                manager.cmd_page(argument)
            
            case "add" | "create":
                logger.info(f"command = {cmd} and argument = {argument}")
                manager.cmd_add(argument)

            case "delete" | "remove":
                logger.info(f"command = {cmd} and argument = {argument}")
                manager.cmd_remove(argument)

            case "priorty":
                logger.info(f"command = {cmd} and argument = {argument}")
                manager.cmd_priorty(argument)
            
            case "status":
                logger.info(f"command = {cmd} and argument = {argument}")
                manager.cmd_status(argument)
            
            case "display":
                logger.info(f"command = {cmd} and argument = {argument}")
                manager.cmd_display(argument)
            
            case "help":
                manager.cmd_help()
                logger.info("Help command received by user")
            
            case "exit" | "Bye":
                logger.info(f"Exit command received by user")
                print("I hope you have Enjoy , Bye have a nice day")
                print("Exiting....")
                Condition = False
            case None | "":
                print("You didn't enter command")
                logger.warning("No command from user")

            case _:
                print("Invalid command")
                logger.error(f"Invalid command received: '{command}'")
            

    except KeyboardInterrupt:
        logger.critical("Keyboard Interrupt by the user")
        print("Exiting....")
        manager.export_data()
        break

    manager.export_data()

logger.info("Program terminated")