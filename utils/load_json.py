import json
import os


def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_abs_path = os.path.join(current_dir, "products.json")
    with open(file_abs_path) as file:
        data = json.load(file)
        return data

