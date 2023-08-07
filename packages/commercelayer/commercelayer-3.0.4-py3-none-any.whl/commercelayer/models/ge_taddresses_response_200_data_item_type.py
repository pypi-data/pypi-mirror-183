from enum import Enum


class GETaddressesResponse200DataItemType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
