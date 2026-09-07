import os

def get_file_content(file_path):
    """
    Get the content of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file.
    """
    if not os.path.isfile(file_path):
        raise ValueError("File not found")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content