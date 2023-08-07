from enum import Enum


class PATCHreturnsreturnIdResponse200DataType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
