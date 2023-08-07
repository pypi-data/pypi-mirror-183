from enum import Enum


class GETvoidsvoidIdResponse200DataRelationshipsReferenceAuthorizationDataType(str, Enum):
    REFERENCE_AUTHORIZATION = "reference_authorization"

    def __str__(self) -> str:
        return str(self.value)
