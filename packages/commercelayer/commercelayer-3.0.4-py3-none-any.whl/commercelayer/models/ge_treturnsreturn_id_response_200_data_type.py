from enum import Enum


class GETreturnsreturnIdResponse200DataType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
