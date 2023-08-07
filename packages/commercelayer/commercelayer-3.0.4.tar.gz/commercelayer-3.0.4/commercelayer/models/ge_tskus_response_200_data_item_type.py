from enum import Enum


class GETskusResponse200DataItemType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
