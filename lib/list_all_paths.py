import os

def list_all_paths(directory):
    """
    List all file paths in the specified directory and its subdirectories.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of all file paths in the directory and its subdirectories.
    """
    all_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            all_paths.append(os.path.join(root, file))
    return all_paths