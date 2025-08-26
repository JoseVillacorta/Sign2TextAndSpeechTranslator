import json
import os
import numpy as np
from src.utils.constants import *

def get_word_ids(words_json_path):
    """
    Gets the list of word IDs from the JSON file
    """
    with open(words_json_path, 'r') as json_file:
        data = json.load(json_file)
    return data['word_ids']

def create_directory_if_not_exists(directory_path):
    """
    Creates the directory if it doesn't exist
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directorio creado: {directory_path}")

def save_json_data(data, file_path):
    """
    Saves data in JSON format
    """
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def load_json_data(file_path):
    """
    Loads data from a JSON file
    """
    with open(file_path, 'r', encoding='utf-8') as json_file:
        return json.load(json_file)