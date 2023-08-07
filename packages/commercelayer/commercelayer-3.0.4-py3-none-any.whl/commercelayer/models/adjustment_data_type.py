from enum import Enum


class AdjustmentDataType(str, Enum):
    ADJUSTMENTS = "adjustments"

    def __str__(self) -> str:
        return str(self.value)
