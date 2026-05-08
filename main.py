import shlex
import logging
from core.logger import start_up
import core.manager as manager
logger = logging.getLogger(__name__)


while True:
    try:
        command = input(manager.command_paths() +">>> ")
        parts = shlex.split(command)
        cmd = parts[0]
        argument = parts[1:]
      
    except KeyboardInterrupt:
        print("Exiting....")
        break

