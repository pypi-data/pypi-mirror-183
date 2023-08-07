from enum import Enum


class AdjustmentCreateDataType(str, Enum):
    ADJUSTMENTS = "adjustments"

    def __str__(self) -> str:
        return str(self.value)
