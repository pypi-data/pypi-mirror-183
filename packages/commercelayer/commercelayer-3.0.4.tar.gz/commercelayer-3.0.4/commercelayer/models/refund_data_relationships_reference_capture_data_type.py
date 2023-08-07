from enum import Enum


class RefundDataRelationshipsReferenceCaptureDataType(str, Enum):
    CAPTURES = "captures"

    def __str__(self) -> str:
        return str(self.value)
