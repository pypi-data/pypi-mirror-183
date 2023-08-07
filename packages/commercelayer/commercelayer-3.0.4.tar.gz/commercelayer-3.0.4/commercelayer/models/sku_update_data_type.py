from enum import Enum


class SkuUpdateDataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
