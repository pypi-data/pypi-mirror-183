from enum import Enum


class CaptureDataRelationshipsReferenceAuthorizationDataType(str, Enum):
    AUTHORIZATIONS = "authorizations"

    def __str__(self) -> str:
        return str(self.value)
