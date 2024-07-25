"""
    All functions related to managing configs.

    Lachlan Paul, 2024
"""
import json
import os

from src.globals import DIRECTORY_FILE


def add_dir(dir_to_add: str, incl_sub_dir: bool = False):
    dir_info = {
        "Location": dir_to_add,
        "Include Sub Directories": incl_sub_dir
    }

    with open(DIRECTORY_FILE, "r+") as file:
        file_data = json.load(file)
        file_data["Directories"].update({os.path.basename(dir_to_add): dir_info})
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.truncate()
