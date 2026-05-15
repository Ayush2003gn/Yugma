import logging
import os
def start_up():
    base = os.path.dirname(os.path.dirname(__file__))
    log_dir = os.path.join(base,"debug")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    log_file = os.path.join(log_dir,"app.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )