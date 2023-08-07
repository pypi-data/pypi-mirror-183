from enum import Enum


class ImportDataType(str, Enum):
    IMPORTS = "imports"

    def __str__(self) -> str:
        return str(self.value)
