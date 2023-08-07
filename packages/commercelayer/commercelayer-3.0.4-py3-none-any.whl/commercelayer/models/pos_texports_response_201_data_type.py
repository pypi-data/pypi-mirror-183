from enum import Enum


class POSTexportsResponse201DataType(str, Enum):
    EXPORTS = "exports"

    def __str__(self) -> str:
        return str(self.value)
