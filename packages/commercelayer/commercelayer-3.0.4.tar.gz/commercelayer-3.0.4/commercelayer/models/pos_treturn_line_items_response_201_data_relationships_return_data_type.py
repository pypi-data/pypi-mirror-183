from enum import Enum


class POSTreturnLineItemsResponse201DataRelationshipsReturnDataType(str, Enum):
    RETURN = "return"

    def __str__(self) -> str:
        return str(self.value)
