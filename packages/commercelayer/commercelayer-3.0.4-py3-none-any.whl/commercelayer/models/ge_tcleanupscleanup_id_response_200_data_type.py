from enum import Enum


class GETcleanupscleanupIdResponse200DataType(str, Enum):
    CLEANUPS = "cleanups"

    def __str__(self) -> str:
        return str(self.value)
