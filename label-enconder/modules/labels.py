"""Auxiliar methods."""
from json import dump


def unique_labels(file, output):
    """
    Get the unic materials at the file.

    Args:
        file: file that contain the filtered labels (clean_labels) related to
        the objects.
        output: file containing a list with the unique words for consulting.

    Returns:
        list containg the unique material labels.
    """
    with open(file, "r") as f:
        words_list = [line.rstrip().split(",")[2].split("|") for line in f]
        words = [i for l in words_list for i in l]
        unique_words = []
        dictionary = {}
        for j in words:
            if j not in unique_words and j:
                unique_words.append(j)
            if j in dictionary:
                dictionary[j] += 1
            else:
                dictionary[j] = 1

        freq_dict = dict(
            sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
        )
        unique_words_s = [key for key in list(freq_dict.keys()) if key != ""]
        with open(output, "w", encoding="UTF-8") as output:
            dump(unique_words_s, output)
        return unique_words_s
