from enum import Enum


class GETordersorderIdResponse200DataRelationshipsRefundsDataType(str, Enum):
    REFUNDS = "refunds"

    def __str__(self) -> str:
        return str(self.value)
