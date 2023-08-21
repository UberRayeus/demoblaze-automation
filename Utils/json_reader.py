import json

def read_json(file_path):
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        raise Exception(f"Error reading JSON file: {e}")