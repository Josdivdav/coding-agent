import requests
import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain.tools import tool

from lib.get_files import get_files
from lib.get_file_content import get_file_content
from lib.create_and_write_file import create_and_write
from lib.list_all_paths import list_all_paths

load_dotenv()

@tool('get_path', description='Return the path of a file in the specified directory', return_direct=False)
def get_path(directory: str, filename: str):
    files = get_files(directory)
    if filename in files:
        return os.path.join(directory, filename)
    else:
        raise ValueError("File not found")

@tool('get_content', description='Return the content of a file output should just be the content', return_direct=False)
def get_content(file_path: str):
    return get_file_content(file_path)

@tool('create_and_write', description='Create a file and write content to it', return_direct=False)
def create_and_write_file(path: str, content: str):
    return create_and_write(path, content)

@tool('list_all_paths', description='List all file paths in the specified directory and its subdirectories', return_direct=False)
def list_all_paths_tool(directory: str):
    return list_all_paths(directory)

agent = create_agent(
    model = 'google_genai:gemini-3.6-flash',
    tools = [get_path, get_content, create_and_write_file, list_all_paths_tool],
)

def main():
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        res = agent.invoke({
            'messages': [
                {'role': 'user', 'content': user_input}
            ]
        })
        
        print(res['messages'][-1].content)
        
if __name__ == "__main__":
    main()