import json

def save_to_json(object: dict, path: str):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(object, f, indent=4)

def load_json_to_dict(path: str):
    with open(path) as json_file:
        return json.load(json_file)
