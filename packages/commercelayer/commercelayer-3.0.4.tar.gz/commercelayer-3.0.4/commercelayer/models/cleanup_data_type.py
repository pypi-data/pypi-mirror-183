from enum import Enum


class CleanupDataType(str, Enum):
    CLEANUPS = "cleanups"

    def __str__(self) -> str:
        return str(self.value)
