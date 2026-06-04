import json
import os

def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
    
def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def ensure_json_file(path):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)

def is_valid_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            json.load(f)
        return True
    except ValueError:
        return False