import logging
from pathlib import Path
import os
import json
logger = logging.getLogger(__name__)

base = os.path.dirname(os.path.dirname(__file__))
datafolder_Path = os.path.join(base, "data") 

def filecategory_finder():
    file_names = []
    file_and_category = {}
    for file in Path(datafolder_Path).glob("*.json"):
        filename = str(file.stem)
        if filename.endswith("_data"):
            category = filename[:-5]
            file_and_category[category] = filename

    return file_and_category

def pathcategory_finder():
    filecategory = filecategory_finder()
    path_category = {}
    if filecategory:
        for file in filecategory:
            datafile = os.path.join(datafolder_Path,filecategory[file]+".json")
            path_category[file] = datafile
    return path_category

def json_to_py(path):
    try:
        with open(path, "r") as f:
            logger.info("taking data from json")
            x = json.load(f)
            return x
    except json.JSONDecodeError:
        logger.error("JSON is corrupted, resetting file", exc_info=True)
        return []
def path_make(filename):
    return os.path.join(datafolder_Path,filename)

def ensure_datafile(file_paths):
    if not os.path.exists(file_paths):
        logger.critical("File is not there")
        with open(file_paths, "w") as f:
            json.dump([], f)


def exporting_data(path,data_list):
    with open(path , "w") as f:
        json.dump(data_list , f , indent= 2 )
        logger.info("Data written to JSON file successfully")