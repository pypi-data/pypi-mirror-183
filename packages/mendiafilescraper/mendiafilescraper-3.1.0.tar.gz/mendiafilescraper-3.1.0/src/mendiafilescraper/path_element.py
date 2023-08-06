from enum import Enum
from pathlib import Path


class PathElement:
    hash_sum = ""

    class ElementType(Enum):
        FILE = 0
        PATH = 1

    type: ElementType


class FileObject(PathElement):
    def __init__(self, file: Path, absolute_file_path: str):
        self.type = self.ElementType.FILE
        self.file = file
        self.absolute_file_path = absolute_file_path

    def __repr__(self):
        out = f"{self.type}, {self.file}, {self.absolute_file_path}, {self.hash_sum}"
        return out


class PathObject(PathElement):
    class SubType(Enum):
        VIDEO_TS = 0

    def __init__(self, path: Path, sub_type: SubType):
        self.type = self.ElementType.PATH
        self.sub_type = sub_type
        self.path = path

    def __repr__(self):
        out = f"{self.type}, {self.sub_type}, {self.path}, {self.hash_sum}"
        return out
