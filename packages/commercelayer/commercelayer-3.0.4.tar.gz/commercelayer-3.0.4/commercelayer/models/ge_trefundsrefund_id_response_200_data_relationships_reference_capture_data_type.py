from enum import Enum


class GETrefundsrefundIdResponse200DataRelationshipsReferenceCaptureDataType(str, Enum):
    REFERENCE_CAPTURE = "reference_capture"

    def __str__(self) -> str:
        return str(self.value)
