from enum import Enum


class POSTpricesResponse201DataRelationshipsPriceListDataType(str, Enum):
    PRICE_LIST = "price_list"

    def __str__(self) -> str:
        return str(self.value)
