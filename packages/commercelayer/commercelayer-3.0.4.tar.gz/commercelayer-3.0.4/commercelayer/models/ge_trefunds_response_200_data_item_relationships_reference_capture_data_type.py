from enum import Enum


class GETrefundsResponse200DataItemRelationshipsReferenceCaptureDataType(str, Enum):
    REFERENCE_CAPTURE = "reference_capture"

    def __str__(self) -> str:
        return str(self.value)
