from enum import Enum


class POSTreturnsResponse201DataType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
