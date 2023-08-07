from enum import Enum


class GETcleanupsResponse200DataItemType(str, Enum):
    CLEANUPS = "cleanups"

    def __str__(self) -> str:
        return str(self.value)
