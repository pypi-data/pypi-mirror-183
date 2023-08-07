from enum import Enum


class POSTfreeGiftPromotionsResponse201DataRelationshipsSkusDataType(str, Enum):
    SKUS = "skus"

    def __str__(self) -> str:
        return str(self.value)
