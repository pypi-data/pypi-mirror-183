from enum import Enum


class POSTwireTransfersResponse201DataType(str, Enum):
    WIRE_TRANSFERS = "wire_transfers"

    def __str__(self) -> str:
        return str(self.value)
