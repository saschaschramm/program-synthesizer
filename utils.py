import os
from typing import Optional
from config import config

def read_file(dir: str, filename: str, extension: str) -> str:
    path: str = os.path.join(dir, f"{filename}.{extension}")
    with open(path, mode="r", encoding="utf-8") as file:
        return file.read()

def write_file(string: str, dir: str, filename: str, extension: str = "txt") -> None:
    path: str = os.path.join(dir, f"{filename}.{extension}")
    with open(path, mode="w", encoding="utf-8") as file:
        file.write(string)

def persist(prompt: str, specification: Optional[str], code: str, filename: str) -> None:
    write_file(prompt, config.TMP_DIR, filename, "prompt")
    if specification is not None:
        write_file(specification, config.TMP_DIR, filename, "spec")
    write_file(code, config.TMP_DIR, filename, "py")
    write_file(code, config.PROGRAM_DIR, "main", "py")