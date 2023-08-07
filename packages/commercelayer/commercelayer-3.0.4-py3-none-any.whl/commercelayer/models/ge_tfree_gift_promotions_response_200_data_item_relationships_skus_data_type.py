from enum import Enum


class GETfreeGiftPromotionsResponse200DataItemRelationshipsSkusDataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
