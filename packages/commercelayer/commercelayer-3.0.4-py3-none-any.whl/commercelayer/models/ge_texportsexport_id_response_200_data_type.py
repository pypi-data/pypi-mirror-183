from enum import Enum


class GETexportsexportIdResponse200DataType(str, Enum):
    EXPORTS = "exports"

    def __str__(self) -> str:
        return str(self.value)
