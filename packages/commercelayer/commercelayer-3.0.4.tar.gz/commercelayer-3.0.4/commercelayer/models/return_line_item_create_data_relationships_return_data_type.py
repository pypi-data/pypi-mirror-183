from enum import Enum


class ReturnLineItemCreateDataRelationshipsReturnDataType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
