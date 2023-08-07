from enum import Enum


class GETcapturescaptureIdResponse200DataRelationshipsRefundsDataType(str, Enum):
    REFUNDS = "refunds"

    def __str__(self) -> str:
        return str(self.value)
