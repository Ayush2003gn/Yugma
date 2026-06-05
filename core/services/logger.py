import logging
import os
from datetime import datetime
from pathlib import Path

def start_up():
    base = Path(os.getenv("APPDATA")) / "Yugma" if os.name == "nt" else Path.home() / ".Yugma"

    log_dir = os.path.join(base, "debug")
    os.makedirs(log_dir, exist_ok=True)

    date = datetime.now().strftime("%Y-%m-%d")
    log_file = os.path.join(log_dir, f"{date}.log")

    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )