from enum import Enum


class VoidDataType(str, Enum):
    VOIDS = "voids"

    def __str__(self) -> str:
        return str(self.value)
