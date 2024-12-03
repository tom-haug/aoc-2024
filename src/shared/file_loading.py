from os.path import exists
from typing import Optional


def load_text_file(file_path: str) -> Optional[str]:
    if not exists(file_path):
        return None
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents.strip("\n")


def load_text_file_lines(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        file_contents = f.read()
    return file_contents.splitlines()


def touch_file(path: str) -> None:
    open(path, "x")


def write_file(path: str, content: str) -> None:
    with open(path, "w") as f:
        f.write(content.strip() + "\n")
