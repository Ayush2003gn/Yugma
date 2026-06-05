import logging
import core.action.action_manager as action
import core.ui.cli.parser.cli_parser as cli_token
import core.renderer.cli.renderer_cli as renderer
logger = logging.getLogger(__name__)



def start_up_loop():
    STORAGE = action.import_storage()
    running = True
    renderer.welcome_message()
    if STORAGE.success is False:
        logger.error(STORAGE.error.error_message)
        renderer.display_error(STORAGE.error.error_message)

    while running:

        try:
            command_input = input(f"{action.command_paths()} > ")
            logger.info(f"User input received: {command_input}")

            if not command_input.strip():
                continue
            parsed_result = cli_token.parse_command(command_input)
            logger.info(f"Tokenized command: {parsed_result}")

            if parsed_result is None:
                logger.warning("Parsed result is None, skipping iteration.")
                renderer.display_error("Failed to parse command. Please try again.")
                continue
        
            if parsed_result.command == "Invalid":
                renderer.display_error(parsed_result.error.error_message)
                continue
            
            if parsed_result.command == "exit" and parsed_result.action == "exit":
                running = False
                STORAGE = action.export_storage()
                renderer.display_exit()
                if STORAGE.success is False:
                    logger.error(STORAGE.error.error_message)
                    renderer.display_error(STORAGE.error.error_message)
                continue
            
            action_result = action.action_manager(parsed_result)
            logger.info(f"Action result: {action_result}")

            action_name = parsed_result.action
            
            renderer.decision_renderer(action_name, action_result)
            STORAGE = action.export_storage()
            if STORAGE.success is False:
                logger.error(STORAGE.error.error_message)
                renderer.display_error(STORAGE.error.error_message)
            
        except KeyboardInterrupt:
            logger.critical("Keyboard Interrupt by the user")
            renderer.display_exit()
            STORAGE = action.export_storage()
            if STORAGE.success is False:
                logger.error(STORAGE.error.error_message)
                renderer.display_error(STORAGE.error.error_message)
            break

        