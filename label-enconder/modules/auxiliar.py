"""Auxiliar methods."""
from json import load
from os import listdir
from os.path import join


def getfiles(data_path: str):
    """Get list of files.

    Args:
        data_path: the unclassified data path.
    """
    files = listdir(data_path)

    return files


def load_json(jsons_path: str, file_name: str):
    """Load a json file from a specific path.

    Args:
        jsons_path: the path os jsons.
        file_name: name of the file that will be loaded.
    """
    file_path = join(jsons_path, file_name)
    with open(file_path, encoding="utf-8") as file:
        data = load(file)

    return data
