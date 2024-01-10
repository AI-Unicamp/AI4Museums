"""Calculate de codes to each material descriptor."""
from modules.labels import unique_labels


def codes(labels_path, output):
    """
    Calculate the binary codes to each label.

    Args:
        labels_path: path to the file containing the labels to be encoded.
        The unique_labels.
        output: file saved to consult the unique words, unique labels.

    Returns:
        A dict with the labels and the respective code.
    """
    labels = unique_labels(labels_path, output)
    code = [pow(2, power) for power in range(0, len(labels))]
    codes_ = dict(zip(labels, code))

    print(codes_)

    return codes_
