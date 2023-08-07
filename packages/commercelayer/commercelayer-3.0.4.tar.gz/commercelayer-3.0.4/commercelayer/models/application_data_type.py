from enum import Enum


class ApplicationDataType(str, Enum):
    APPLICATION = "application"

    def __str__(self) -> str:
        return str(self.value)
