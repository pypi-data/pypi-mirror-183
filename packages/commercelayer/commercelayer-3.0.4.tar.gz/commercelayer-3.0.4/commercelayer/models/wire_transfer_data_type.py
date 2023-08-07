from enum import Enum


class WireTransferDataType(str, Enum):
    WIRE_TRANSFERS = "wire_transfers"

    def __str__(self) -> str:
        return str(self.value)
