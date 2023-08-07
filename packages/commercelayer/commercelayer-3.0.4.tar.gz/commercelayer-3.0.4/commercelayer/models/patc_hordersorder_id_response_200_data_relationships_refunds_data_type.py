from enum import Enum


class PATCHordersorderIdResponse200DataRelationshipsRefundsDataType(str, Enum):
    REFUNDS = "refunds"

    def __str__(self) -> str:
        return str(self.value)
