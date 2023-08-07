from enum import Enum


class PromotionDataType(str, Enum):
    PROMOTIONS = "promotions"

    def __str__(self) -> str:
        return str(self.value)
