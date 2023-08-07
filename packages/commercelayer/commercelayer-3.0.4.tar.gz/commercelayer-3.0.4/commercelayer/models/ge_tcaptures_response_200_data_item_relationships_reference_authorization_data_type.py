from enum import Enum


class GETcapturesResponse200DataItemRelationshipsReferenceAuthorizationDataType(str, Enum):
    REFERENCE_AUTHORIZATION = "reference_authorization"

    def __str__(self) -> str:
        return str(self.value)
