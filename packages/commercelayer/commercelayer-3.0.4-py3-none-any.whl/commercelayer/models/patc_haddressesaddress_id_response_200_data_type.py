from enum import Enum


class PATCHaddressesaddressIdResponse200DataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
