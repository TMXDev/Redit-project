import json

def save_api_keys(api_keys):
    with open('api_keys.json', 'w') as f:
        json.dump(api_keys, f)

def load_api_keys():
    try:
        with open('api_keys.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
