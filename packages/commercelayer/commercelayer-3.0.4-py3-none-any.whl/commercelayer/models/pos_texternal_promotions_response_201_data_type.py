from enum import Enum


class POSTexternalPromotionsResponse201DataType(str, Enum):
    EXTERNAL_PROMOTIONS = "external_promotions"

    def __str__(self) -> str:
        return str(self.value)
