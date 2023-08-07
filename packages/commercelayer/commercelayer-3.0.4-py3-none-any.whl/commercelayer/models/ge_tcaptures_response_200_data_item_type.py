from enum import Enum


class GETcapturesResponse200DataItemType(str, Enum):
    CAPTURES = "captures"

    def __str__(self) -> str:
        return str(self.value)
