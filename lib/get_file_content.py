import os

def get_file_content(file_path):
    if not os.path.isfile(file_path):
        raise ValueError("File not found")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content
