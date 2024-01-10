"""Constants to help the modules."""

from os import getcwd
from os.path import join

ROOT_DIR = getcwd()
DATA = join(ROOT_DIR, "data")
ORIGINAL_DB = join(DATA, "originaldb")
ENCODED_DB = join(DATA, "encodeddb")
ENCODED_LABELS = join(DATA, "encoded_labels.txt")
