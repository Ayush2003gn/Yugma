import logging
import core.renderer.cli.renderer_cli as renderer_cli
logger = logging.getLogger(__name__)


logger = logging.getLogger(__name__)


def start_up_loop():
    running = True
    while running:
        try:
            renderer_cli.start_cli()

        except KeyboardInterrupt:
            logger.critical("Keyboard Interrupt by the user")
            print("Exiting....")
            break

        