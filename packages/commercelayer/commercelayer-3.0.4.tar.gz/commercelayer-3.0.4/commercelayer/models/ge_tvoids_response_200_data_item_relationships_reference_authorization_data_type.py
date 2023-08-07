from enum import Enum


class GETvoidsResponse200DataItemRelationshipsReferenceAuthorizationDataType(str, Enum):
    REFERENCE_AUTHORIZATION = "reference_authorization"

    def __str__(self) -> str:
        return str(self.value)
