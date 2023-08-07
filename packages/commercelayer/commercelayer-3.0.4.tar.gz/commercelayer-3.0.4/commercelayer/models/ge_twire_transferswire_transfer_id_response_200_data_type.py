from enum import Enum


class GETwireTransferswireTransferIdResponse200DataType(str, Enum):
    WIRE_TRANSFERS = "wire_transfers"

    def __str__(self) -> str:
        return str(self.value)
