import logging
import core.action.action_manager as action
import core.ui.cli.parser.cli_parser as cli_token
import core.renderer.cli.renderer_cli as renderer
logger = logging.getLogger(__name__)



def start_up_loop():

    running = True
    renderer.welcome_message()

    while running:

        try:
            command_input = input(f"{action.command_paths()} > ")
            logger.info(f"User input received: {command_input}")

            if not command_input.strip():
                continue
            parsed_result = cli_token.parse_command(command_input)
            logger.info(f"Tokenized command: {parsed_result}")

           
            if parsed_result.command == "Invalid":
                renderer.display_error(parsed_result.error.error_message)
                continue
            
            if parsed_result.command == "exit" and parsed_result.action == "exit":
                running = False
                renderer.display_exit()
                continue
            
            action_result = action.action_manager(parsed_result)
            logger.info(f"Action result: {action_result}")

            action_name = parsed_result.action
            
            renderer.decision_renderer(action_name, action_result)
            
        except KeyboardInterrupt:
            logger.critical("Keyboard Interrupt by the user")
            renderer.display_exit()
            break

        