from enum import Enum


class AdjustmentUpdateDataType(str, Enum):
    ADJUSTMENTS = "adjustments"

    def __str__(self) -> str:
        return str(self.value)
