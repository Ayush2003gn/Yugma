import os
from pathlib import Path
import logging
logger = logging.getLogger(__name__)

def get_data_folder():
    base = os.path.dirname(__file__)
    logger.info(f"path to base: {base} ")
    return os.path.join(base,"data")

def list_data_files():
    data_folder = get_data_folder()
    return os.listdir(data_folder)

def get_page_file(page_name):
    logger.info(f"page name: {page_name}")
    data_folder = get_data_folder()

    for i in [" ","/","\\","."]:
        page_name = page_name.replace(i,"_")
    page_name = page_name.lower()+"_data.json"
    return os.path.join(data_folder,page_name)

def ensure_data_folder_directory():
    data_folder = get_data_folder()
    Path(data_folder).mkdir(parents=True, exist_ok=True)

def ensure_data_file_directory(file_path):
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    