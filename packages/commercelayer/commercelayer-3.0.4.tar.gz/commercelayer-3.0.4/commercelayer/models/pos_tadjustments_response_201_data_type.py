from enum import Enum


class POSTadjustmentsResponse201DataType(str, Enum):
    ADJUSTMENTS = "adjustments"

    def __str__(self) -> str:
        return str(self.value)
