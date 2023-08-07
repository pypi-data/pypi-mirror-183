from enum import Enum


class RefundDataType(str, Enum):
    REFUNDS = "refunds"

    def __str__(self) -> str:
        return str(self.value)
