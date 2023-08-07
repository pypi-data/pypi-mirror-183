from enum import Enum


class POSTcleanupsResponse201DataType(str, Enum):
    CLEANUPS = "cleanups"

    def __str__(self) -> str:
        return str(self.value)
