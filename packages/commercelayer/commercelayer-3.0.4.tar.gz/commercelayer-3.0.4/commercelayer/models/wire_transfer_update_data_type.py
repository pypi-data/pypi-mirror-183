from enum import Enum


class WireTransferUpdateDataType(str, Enum):
    WIRE_TRANSFERS = "wire_transfers"

    def __str__(self) -> str:
        return str(self.value)
