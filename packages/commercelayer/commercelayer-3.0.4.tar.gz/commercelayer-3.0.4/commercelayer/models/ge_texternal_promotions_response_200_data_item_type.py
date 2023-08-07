from enum import Enum


class GETexternalPromotionsResponse200DataItemType(str, Enum):
    EXTERNAL_PROMOTIONS = "external_promotions"

    def __str__(self) -> str:
        return str(self.value)
