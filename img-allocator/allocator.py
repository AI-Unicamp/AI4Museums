"""Allocating the images accordingly to their specific code."""
import os
from os import makedirs
from os.path import basename, exists, isdir, join
from shutil import copyfile

from constants import DATA, ENCODED_DB, ENCODED_LABELS, ORIGINAL_DB


def load_file(data_path: str, txt_file: str):
    """Load the txt by lines with the encoded labels.

    Args:
        file_path: the path os jsons.
        file_name: name of the file that will be loaded.
    """
    file_path = join(data_path, txt_file)
    with open(file_path, encoding="utf-8") as file:
        lines = [line.rstrip() for line in file]

    return lines


def src_db(source: str):
    """Make a list with the path of the original image database files.

    Read the whole originalbd folder and make a list of the path of each
    image file.

    Args:
        source: path of the folder containing the original image database. In
        this case the orignalbd.

    """
    source_list = []
    for root, _, files in os.walk(source):
        for file in files[:]:
            source_list.append(tuple((join(root, file), basename(file))))

    return source_list


def coded_db(codes: str, source_db: str, dest_db):
    """Create de folder enconded database.

    Creates the folders encoded and copy all relative files. For example, the
    image MCHE_59442 corresponds to the code 2, will create a folder named
    2 if not exists and them copy the images corresponding to MCHE_59442.

    Args:
        codes: file containing the codes (encoded_labels.txt)
        source_db: originaldb folder containing the original image database
    """
    with open(codes, "rt") as f:
        code_lines = f.read().splitlines()
    for line in code_lines:
        code = line.split("|")[2]
        folder_code = join(dest_db, code)
        if not isdir(folder_code):
            makedirs(folder_code)
        for (src_path, name) in src_db(source_db):
            name_id = "".join([name.split("_")[0], "_", name.split("_")[1]])
            if name_id in line:
                if not exists(join(folder_code, name)):
                    copyfile(src_path, join(folder_code, name))


coded_db(ENCODED_LABELS, ORIGINAL_DB, ENCODED_DB)
