from enum import Enum


class GETapplicationapplicationIdResponse200DataType(str, Enum):
    APPLICATION = "application"

    def __str__(self) -> str:
        return str(self.value)
