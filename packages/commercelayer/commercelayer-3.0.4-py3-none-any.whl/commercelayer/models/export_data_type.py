from enum import Enum


class ExportDataType(str, Enum):
    EXPORTS = "exports"

    def __str__(self) -> str:
        return str(self.value)
