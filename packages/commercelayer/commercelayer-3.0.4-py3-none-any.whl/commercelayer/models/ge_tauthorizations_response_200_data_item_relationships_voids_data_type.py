from enum import Enum


class GETauthorizationsResponse200DataItemRelationshipsVoidsDataType(str, Enum):
    VOIDS = "voids"

    def __str__(self) -> str:
        return str(self.value)
