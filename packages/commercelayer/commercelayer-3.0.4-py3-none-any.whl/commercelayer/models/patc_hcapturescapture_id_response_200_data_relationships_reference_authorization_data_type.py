from enum import Enum


class PATCHcapturescaptureIdResponse200DataRelationshipsReferenceAuthorizationDataType(str, Enum):
    REFERENCE_AUTHORIZATION = "reference_authorization"

    def __str__(self) -> str:
        return str(self.value)
