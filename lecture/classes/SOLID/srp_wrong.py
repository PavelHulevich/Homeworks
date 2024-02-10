from pathlib import Path
from zipfile import ZipFile

from typing import TypedDict


class UserDTO(TypedDict):
    first_name: str
    last_name: str


"""
В этом примере у вашего класса файлового менеджера есть две разные обязанности. Он использует методы .read() и .write()
для управления файлом. Он также работает с ZIP-архивами, предоставляя методы .compress() и .decompress().
Этот класс нарушает принцип единой ответственности, поскольку у него есть две причины для изменения своей внутренней 
реализации. 
"""


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
