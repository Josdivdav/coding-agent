# File Agent CLI

A simple command-line agent built with [LangChain](https://python.langchain.com/) that can browse, read, and write files on the local filesystem using natural-language commands. The agent is powered by Google's Gemini model (`gemini-3.6-flash`) and exposes a small set of filesystem tools it can call autonomously to satisfy a request.

## Features

- **Interactive REPL** – type commands in plain English and the agent decides which tools to use.
- **File discovery** – list every file path under a directory (recursively).
- **Path lookup** – resolve a filename to its full path within a given directory.
- **File reading** – fetch the contents of a file.
- **File writing** – create a new file and write content to it.

## How It Works

The script wires up four custom tools and hands them to a LangChain agent (`create_agent`). On each turn, the agent reads your input, decides whether it needs to call one or more tools, executes them, and returns a final response.

### Tools

| Tool | Description | Backing function |
|---|---|---|
| `get_path` | Returns the path of a file in a specified directory | `lib.get_files.get_files` |
| `get_content` | Returns the content of a file | `lib.get_file_content.get_file_content` |
| `create_and_write` | Creates a file and writes content to it | `lib.create_and_write_file.create_and_write` |
| `list_all_paths` | Lists all file paths in a directory and its subdirectories | `lib.list_all_paths.list_all_paths` |

## Project Structure

```
.
├── main.py                     # Entry point / agent setup (this script)
├── .env                        # Environment variables (not committed)
└── lib/
    ├── get_files.py
    ├── get_file_content.py
    ├── create_and_write_file.py
    └── list_all_paths.py
```

> Note: the `lib/` modules (`get_files`, `get_file_content`, `create_and_write`, `list_all_paths`) are expected to already exist in your project and implement the actual filesystem logic used by each tool.

## Requirements

- Python 3.10+
- A Google AI API key with access to the Gemini model family
- Dependencies:
  - `langchain`
  - `python-dotenv`
  - `requests`
  - Whatever Google GenAI integration package `langchain` uses under the hood for the `google_genai:` model provider prefix

Install dependencies, for example:

```bash
pip install langchain python-dotenv requests langchain-google-genai
```

(Adjust package names to match whichever LangChain/Google GenAI integration version you're using.)

## Environment Variables

Create a `.env` file in the project root with the credentials required by the Google GenAI provider, for example:

```
GOOGLE_API_KEY=your_api_key_here
```

The script loads this automatically via `load_dotenv()`.

## Usage

Run the script:

```bash
python main.py
```

You'll see a prompt:

```
Enter a command (or 'exit' to quit):
```

Type a natural-language instruction, and the agent will use its tools as needed. Examples:

```
Enter a command (or 'exit' to quit): List all the files in the ./data directory
Enter a command (or 'exit' to quit): Show me the content of config.json in ./data
Enter a command (or 'exit' to quit): Create a file called notes.txt in ./data with the text "Hello world"
```

Type `exit` to quit the loop.

## Notes & Caveats

- **Model name**: `gemini-3.6-flash` should match an actual available Gemini model identifier for your account/region — update this string if the model name differs.
- **Error handling**: `get_path` raises a `ValueError` if the file isn't found; consider wrapping tool calls with try/except if you want friendlier error messages surfaced back to the user.
- **Security**: `create_and_write` and `get_content` operate directly on the filesystem with whatever path the agent decides to use. If you expose this to untrusted input, sandbox the working directory to avoid unintended reads/writes outside your project.
- **Indentation**: double check the tool function bodies (`get_path`, `get_content`, etc.) are consistently indented in your actual source file — mixed indentation will cause `IndentationError` in Python.
