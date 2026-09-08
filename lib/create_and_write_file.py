import os

def create_and_write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as file:
        file.write(content)
    return f"File created and written to at: {path}"
