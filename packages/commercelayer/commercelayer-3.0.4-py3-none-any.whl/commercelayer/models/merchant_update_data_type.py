from enum import Enum


class MerchantUpdateDataType(str, Enum):
    MERCHANTS = "merchants"

    def __str__(self) -> str:
        return str(self.value)
