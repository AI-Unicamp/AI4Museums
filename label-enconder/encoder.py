"""Extract the raw metada field from every json file, object."""
from os.path import isdir, join

import click

from modules.auxiliar import getfiles, load_json
from modules.codes import codes
from modules.constants import (
    CLEAN_LABELS,
    ENCODED_LABELS,
    JSONS_PATH,
    MATERIAL_PATTERN,
    METATADA_KEY,
    PROJECT_PATH,
    RAW_LABELS,
    TARGET_VALUE,
    UNIQUE_WORDS,
)


class NaturalOrderGroup(click.Group):
    """Command group to list subcommands in the order they were added."""

    def list_commands(self, ctx):
        """List command names as they are in commands dict."""
        ctx.ensure_object(dict)
        return self.commands.keys()


@click.group(cls=NaturalOrderGroup)
def main():
    """Encode material descriptors."""


@main.command("raw_labels")
@click.option("--jsons_path", "-j", default=JSONS_PATH, help="Path of the jsons file.")
@click.option("--metadata", "-m", default=METATADA_KEY, help="The metadata field.")
@click.option(
    "--pattern",
    "-p",
    default=MATERIAL_PATTERN,
    help="The pattern of the field to match.",
)
def get_raw_labels(jsons_path: str, metadata: str, pattern: str):
    """Get the description of the material label.

    Args:
        jsons_path: path of the jsons file.
        metadata: metadata field.
        pattern: pattern of the field to match.

    Returns:
        list: list of lists that contains the museum acr and file
        id, the field founded to match and the target value.
    """
    if not isdir(join(PROJECT_PATH, RAW_LABELS)):
        labels = []
        with open(join(PROJECT_PATH, RAW_LABELS), "w", encoding="UTF-8") as output:
            for item in getfiles(jsons_path):
                file = load_json(jsons_path, item)
                FIELD = "".join(str(_) for _ in file[metadata] if pattern in _)
                labels.append(
                    [item.split(".")[0], FIELD, file[metadata][FIELD][TARGET_VALUE]]
                )
                output.write(
                    f"{item.split('.')[0]}, {FIELD}, {file[metadata][FIELD][TARGET_VALUE]}\n"
                )

        return labels
    print("The raw labels already exists")


@main.command("encode")
@click.option("--labels_in", "-i", default=CLEAN_LABELS, help="Filtered labels")
@click.option(
    "--labels_out", "-o", default=ENCODED_LABELS, help="Output with the encoded labels"
)
def encoding(labels_in, labels_out):
    """Encode all clean labels.

    At this stage all the labels will be ready to use.
    Args:
        labels_in: the filtered labels to be enconded.
        labels_out: file with the final encoded labels.
    """

    try:
        encode_dict = codes(CLEAN_LABELS, UNIQUE_WORDS)
        print(encode_dict)
        with open(labels_in, encoding="utf-8") as file:
            with open(labels_out, "w", encoding="UTF-8") as output:
                lines = file.read().splitlines()
                labels = [(line.split(",")[0], line.split(",")[2]) for line in lines]
                items_id = list(enumerate(labels))
                for i, j in items_id:
                    each = list(j[1].split("|"))
                    encode_count = 0
                    for i in each:
                        if i in encode_dict.keys():
                            encode_count += encode_dict[i]
                    output.write(f"{j[0]},{each},{encode_count}\n")
    except FileNotFoundError:
        print("There's no data to parse.\n")
        print("It's necessary to create de clean labels first.")
        print("It's possible to that running the raw_labels module first")
        print("and then refine manually, excluding the greater then signal,")
        print("synonym words, and etc.")


if __name__ == "__main__":
    main()
