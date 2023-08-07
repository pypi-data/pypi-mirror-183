from enum import Enum


class PATCHpackagespackageIdResponse200DataRelationshipsStockLocationDataType(str, Enum):
    STOCK_LOCATION = "stock_location"

    def __str__(self) -> str:
        return str(self.value)
