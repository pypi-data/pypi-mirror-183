from enum import Enum


class GETadjustmentsResponse200DataItemType(str, Enum):
    ADJUSTMENTS = "adjustments"

    def __str__(self) -> str:
        return str(self.value)
