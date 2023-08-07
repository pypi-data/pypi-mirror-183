from enum import Enum


class POSTorderCopiesResponse201DataRelationshipsTargetOrderDataType(str, Enum):
    TARGET_ORDER = "target_order"

    def __str__(self) -> str:
        return str(self.value)
