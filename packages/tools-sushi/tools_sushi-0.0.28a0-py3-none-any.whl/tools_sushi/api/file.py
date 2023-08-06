import os
from typing import Optional


def read_file(file_name: str, encoding: Optional[str] = 'utf8') -> str:
    """opens file and returns all data from file in str"""

    try:
        with open(file=file_name, encoding=encoding) as f:
            return f.readlines()
    except FileNotFoundError:
        print("[sushi] file not found")
        exit(1)
    except LookupError:
        print("[sushi] unknown encoding")
        exit(1)


def append_to_file(file_name: str, content: str, encoding: Optional[str] = 'utf8'):
    """append to file and create it if it doesnt exists"""

    with open(file=file_name, mode='a', encoding=encoding) as f:
        return f.write(content)


def create_file(file_name: str) -> None:
    """creates empty file"""

    with open(file=file_name, mode='w') as f:
        return f.write("")


def get_file_size(file_name: str):
    """return file size in bytes"""

    try:
        return os.path.getsize(file_name)
    except FileNotFoundError:
        print("[sushi] file not found")
        exit(1)


def delete_file(file_name: str) -> None:
    """delete file"""

    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("[sushi] file not found")
        exit(1)
