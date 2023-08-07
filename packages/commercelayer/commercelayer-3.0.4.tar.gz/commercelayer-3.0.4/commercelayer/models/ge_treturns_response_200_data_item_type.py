from enum import Enum


class GETreturnsResponse200DataItemType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
