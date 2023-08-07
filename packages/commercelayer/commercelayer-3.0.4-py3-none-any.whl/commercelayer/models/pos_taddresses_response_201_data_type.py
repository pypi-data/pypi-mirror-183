from enum import Enum


class POSTaddressesResponse201DataType(str, Enum):
    ADDRESSES = "addresses"

    def __str__(self) -> str:
        return str(self.value)
