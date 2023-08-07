from enum import Enum


class GETadjustmentsadjustmentIdResponse200DataType(str, Enum):
    ADJUSTMENTS = "adjustments"

    def __str__(self) -> str:
        return str(self.value)
