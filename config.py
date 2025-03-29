import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    API_KEYS_FILE = 'api_keys.json'
