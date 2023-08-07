from enum import Enum


class GETreturnLineItemsResponse200DataItemRelationshipsReturnDataType(str, Enum):
    RETURN = "return"

    def __str__(self) -> str:
        return str(self.value)
