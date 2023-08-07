from enum import Enum


class CleanupCreateDataType(str, Enum):
    CLEANUPS = "cleanups"

    def __str__(self) -> str:
        return str(self.value)
