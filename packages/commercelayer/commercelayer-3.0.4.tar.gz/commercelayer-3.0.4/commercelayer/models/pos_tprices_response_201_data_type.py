from enum import Enum


class POSTpricesResponse201DataType(str, Enum):
    PRICES = "prices"

    def __str__(self) -> str:
        return str(self.value)
