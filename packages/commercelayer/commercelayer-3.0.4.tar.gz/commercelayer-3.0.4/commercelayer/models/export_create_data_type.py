from enum import Enum


class ExportCreateDataType(str, Enum):
    EXPORTS = "exports"

    def __str__(self) -> str:
        return str(self.value)
