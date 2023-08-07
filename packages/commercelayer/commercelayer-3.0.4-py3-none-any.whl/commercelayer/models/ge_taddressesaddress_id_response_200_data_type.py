from enum import Enum


class GETaddressesaddressIdResponse200DataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
