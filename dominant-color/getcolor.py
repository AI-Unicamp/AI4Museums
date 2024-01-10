"""Get the color name."""

from os import getcwd, listdir, makedirs
from os.path import exists, isdir, join
from shutil import move
import click
from tqdm import tqdm
from colornamer import get_color_from_rgb
from colorthief import ColorThief

PROJECT_PATH = getcwd()
DATA_PATH = join(PROJECT_PATH, "data")


def getfiles(data_path: str):
    """Get list of files.

    Args:
        data_path: the unclassified data path.
    """
    files = [
        (listdir(join(data_path, i)),
         join(data_path, i)) for i in list(listdir(data_path))
    ]

    return files


@click.command()
@click.option('--data_path', '-d',
              default=DATA_PATH,
              help='Path of the unclassified data')
def color_name(data_path: str):
    """Get color name and alocate to the respective folder.

    Args:
        images: list of images for every folder.
    """

    for file, folder in tqdm(getfiles(data_path)):
        for item in file:
            try:
                color_thief = ColorThief(join(folder, item))
                dominant_color = color_thief.get_color(quality=1)
                color_group = get_color_from_rgb(dominant_color)["common_color"]
            except Exception as err:
                print(f"Image not classified!{err},Image:{join(folder, item)}")
                print("Moving to empty pixels folder...")
                move(join(folder, item), join(PROJECT_PATH, "empty_pixels"))
                continue
            if not isdir(join(folder, color_group)):
                makedirs(join(folder, color_group), exist_ok=True)

            if not exists(join(folder, color_group, item)):
                move(join(folder, item), join(folder, color_group))


if __name__ == '__main__':
    color_name()
