from enum import Enum


class POSTskusResponse201DataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
