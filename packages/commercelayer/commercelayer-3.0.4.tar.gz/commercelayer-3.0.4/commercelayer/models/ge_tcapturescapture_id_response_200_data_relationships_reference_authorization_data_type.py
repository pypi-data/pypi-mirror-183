from enum import Enum


class GETcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationDataType(str, Enum):
    REFERENCE_AUTHORIZATION = "reference_authorization"

    def __str__(self) -> str:
        return str(self.value)
