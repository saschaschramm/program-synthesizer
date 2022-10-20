import json
import os
import shutil

from typing import Any


def read_file(path: str) -> Any:
    with open(path, mode="r", encoding="utf-8") as file:
        extension: str = os.path.splitext(path)[-1]
        if extension == ".json":
            return json.load(file)
        else:
            return file.read()


def write_file(path, string) -> None:
    with open(path, mode="w", encoding="utf-8") as file:
        file.write(string)


def write_json(path: str, dict: dict) -> None:
    with open(path, mode="w", encoding="utf-8") as file:
        json.dump(dict, file, indent=4)


def filename(index: int) -> str:
    return f"{(index)*10:04d}"


def make_dir(dir: str) -> None:
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
