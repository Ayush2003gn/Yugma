import logging
import core.action as action
import core.ui.cli.token as cli_token
import core.renderer.cli.renderer_cli as renderer
logger = logging.getLogger(__name__)



def start_up_loop():
    running = True
    renderer.welcome_message()
    while running:
        try:
            command_input = input(f"{action.command_paths()} > ")
            logger.info(f"User input received: {command_input}")

            cmd,arguments = cli_token.parse_command(command_input)
            logger.info(f"Tokenized command: {cmd}, Arguments: {arguments}")

            result_command_handler = cli_token.command_handler(cmd, arguments)
            
            if result_command_handler is None:
                continue
            
            if result_command_handler["command"] == "exit":
                running = False
                continue
            
            result = action.execute_command(result_command_handler)
            logger.info(f"Action result: {result}")

            action_name = result_command_handler["action"]
            
            renderer.decision_renderer(action_name, result)

        except KeyboardInterrupt:
            logger.critical("Keyboard Interrupt by the user")
            print("Exiting....")
            break

        