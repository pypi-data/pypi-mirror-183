from enum import Enum


class ExternalPromotionUpdateDataType(str, Enum):
    EXTERNAL_PROMOTIONS = "external_promotions"

    def __str__(self) -> str:
        return str(self.value)
