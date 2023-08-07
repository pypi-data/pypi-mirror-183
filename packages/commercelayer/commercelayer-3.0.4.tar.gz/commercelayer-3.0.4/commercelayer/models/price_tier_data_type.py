from enum import Enum


class PriceTierDataType(str, Enum):
    PRICE_TIERS = "price_tiers"

    def __str__(self) -> str:
        return str(self.value)
