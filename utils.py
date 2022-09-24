import json
import os
import shutil
from typing import Optional


def read_file_with_path(path: str) -> str:
    with open(path, mode="r", encoding="utf-8") as file:
        extension: str = os.path.splitext(path)[-1]
        if extension == ".json":
            return json.load(file)
        else:
            return file.read()


def read_file(dir: str, filename: str, extension: str) -> str:
    path: str = os.path.join(dir, f"{filename}.{extension}")
    return read_file_with_path(path)


def write_file(string: str, dir: str, filename: str, extension: str) -> None:
    path: str = os.path.join(dir, f"{filename}.{extension}")
    with open(path, mode="w", encoding="utf-8") as file:
        file.write(string)


def persist(
    prompt: Optional[str], program: str, tmp_dir: Optional[str], filename: str
) -> None:

    if prompt is not None:
        write_file(prompt, tmp_dir, filename, "prompt")

    write_file(program, tmp_dir, filename, "py")
    write_file(program, tmp_dir, "main", "py")


def make_dir(dir: str) -> None:
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)


def initalize(target_dir: str, program: Optional[str] = None) -> None:
    write_file(program.strip(), target_dir, "main", "py")
    write_file(program.strip(), target_dir, "0000", "py")
