import os
from pathlib import Path
import logging
import json
logger = logging.getLogger(__name__)

def get_data_folder():
    base = Path(os.getenv("APPDATA")) / "Yugma" if os.name == "nt" else Path.home() / ".Yugma"
    logger.info(f"path to base: {base} ")
    return os.path.join(base,"data")

def create_check_data_folder():
    data_folder = get_data_folder()
    if not os.path.exists(data_folder):
        try:
            os.makedirs(data_folder)
            return None
        except Exception as e:
            logger.error(str(e))
            return "Error creating data folder"

def ensure_data_folder_directory():
    data_folder = get_data_folder()
    try:
        Path(data_folder).mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logger.error(str(e))

def ensure_data_file_directory(file_path):
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        logger.error(str(e))

def file_exists(file_path):
    return Path(file_path).is_file()

def create_file(file_path):
    try:
        ensure_data_file_directory(file_path)

        if not Path(file_path).exists():
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump({"pages": []}, f)

    except Exception as e:
        logger.error(str(e))

def delete_file(file_path):
    try:
        if Path(file_path).exists():
            Path(file_path).unlink()
    except Exception as e:
        logger.error(str(e))

def config_file():
    data_folder = get_data_folder()
    configfiles = os.path.join(data_folder,"config.json")
    file_exists = os.path.exists(configfiles)
    if not file_exists:
        create_file(configfiles)
    return configfiles