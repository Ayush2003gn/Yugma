import logging
import core.ui.cli.loop as cli_loop
logger = logging.getLogger(__name__)   

def start():
    logger.info("Starting Yukta application")
    cli_loop.start_up_loop()

    