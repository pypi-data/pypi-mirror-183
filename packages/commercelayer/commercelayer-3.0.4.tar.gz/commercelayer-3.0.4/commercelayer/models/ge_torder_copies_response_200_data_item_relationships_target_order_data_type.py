from enum import Enum


class GETorderCopiesResponse200DataItemRelationshipsTargetOrderDataType(str, Enum):
    TARGET_ORDER = "target_order"

    def __str__(self) -> str:
        return str(self.value)
