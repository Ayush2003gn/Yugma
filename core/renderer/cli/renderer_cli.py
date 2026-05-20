import logging

import core.action as action

import core.ui.cli.token as cli_token
logger = logging.getLogger(__name__)

def start_cli():
    logger.info("Starting CLI renderer")
    taskpage = action.todo
    logger.info("Task page initialized")
    while True:
        user_input = input("Enter command: ")
        logger.info(f"User input received: {user_input}")
        token_return = cli_token.parse_command(user_input)
        logger.info(f"Token return from parser: {token_return}")
        if token_return is None:
            logger.warning("Invalid command format")
            print("Invalid command format. Please try again.")
            continue
        cmd, argument = token_return
        command_handler_result = cli_token.command_handler(cmd, argument)
        logger.info(f"Command handler result: {command_handler_result}")
        result = action.ui_return_to_action(command_handler_result)
        logger.info(f"Result from action handler: {result}")
        if result["success"]:
            print(result["message"])
        else:
            print(f"Error: {result['message']}")
            logger.error(f"Error occurred: {result['message']}")
