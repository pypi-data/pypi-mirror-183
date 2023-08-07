from enum import Enum


class PATCHcustomerscustomerIdResponse200DataRelationshipsReturnsDataType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
