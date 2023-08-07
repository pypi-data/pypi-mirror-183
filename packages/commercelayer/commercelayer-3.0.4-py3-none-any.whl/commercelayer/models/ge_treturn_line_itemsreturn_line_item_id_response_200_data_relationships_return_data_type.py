from enum import Enum


class GETreturnLineItemsreturnLineItemIdResponse200DataRelationshipsReturnDataType(str, Enum):
    RETURN = "return"

    def __str__(self) -> str:
        return str(self.value)
