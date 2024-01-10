"""Constants for the whole project."""

from os import getcwd
from os.path import join

# DATA = join(getcwd(), 'data', 'jsons')
PROJECT_PATH = getcwd()

DATA = join(PROJECT_PATH, "data")
RAW = join(DATA, "raw")
INTERIM = join(DATA, "interim")
PROCESSED = join(DATA, "processed")
ENCODED_LABELS = join(PROCESSED, "encoded_labels.txt")
UNIQUE_LABELS = join(PROCESSED, "unique_labels.txt")
UNIQUE_WORDS = join(PROCESSED, "unique_words.txt")
JSONS_PATH = join(RAW, "jsons")
CLEAN_LABELS = join(INTERIM, "clean_labels.txt")
MATERIAL_PATTERN = "materia"
METATADA_KEY = "metadata"
TARGET_VALUE = "value_as_string"
RAW_LABELS = join(RAW, "raw_labels.txt")
