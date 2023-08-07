from enum import Enum


class POSTmarketsResponse201DataRelationshipsPriceListDataType(str, Enum):
    PRICE_LIST = "price_list"

    def __str__(self) -> str:
        return str(self.value)
