import logging
import core.services.logger 
import core.manager as manager
core.services.logger.start_up()
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Starting the application")
    manager.start()
    logger.info("Application has been terminated")