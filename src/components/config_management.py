"""
    All functions related to managing configs.

    Lachlan Paul, 2024
"""
import json
import os

from src.globals import DIRECTORY_FILE


def add_dir(dir: str):
    with open(DIRECTORY_FILE, "r") as file:
        data = json.load(file)
    dir_to_add = {os.path.basename: dir}
    data.update(dir_to_add)

    with open(DIRECTORY_FILE, 'w') as file:
        json.dump(data, file, indent=4)