import os

def create_and_write(path, content):
    """
    Create a file at the specified path and write content to it.

    Args:
        path (str): The path where the file will be created.
    Returns:
        str: A message indicating the file was created and written to.
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    # Write content to the file
    with open(path, 'w') as file:
        file.write(content)
    return f"File created and written to at: {path}"