import logging
from pathlib import Path
import os
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
