import logging
import core.ui.cli.token as token


logger = logging.getLogger(__name__)


def start_up_loop():
    running = True
    while running:
        try:
            command = input("token.command_paths()" +">>> ")
            cmd, argument = token.command_breakdown(command)
            parsed = token.command_handler(cmd, argument)

        except KeyboardInterrupt:
            logger.critical("Keyboard Interrupt by the user")
            print("Exiting....")
            break

        