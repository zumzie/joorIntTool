# util/utils.py
import json

def process_data(json_data):
    # Assume json_data is a JSON string; convert it to a Python dict
    data = json.loads(json_data)
    # Remap data as needed
    remapped_data = [{ "new_key": item["old_key"] for item in data }]
    return json.dumps(remapped_data)  # Convert back to JSON string
