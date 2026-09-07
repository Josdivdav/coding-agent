import os


def get_files(directory):
    """
    Get a list of files in the specified directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of files in the directory.
    """
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]