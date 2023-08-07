from enum import Enum


class GETauthorizationsauthorizationIdResponse200DataRelationshipsVoidsDataType(str, Enum):
    VOIDS = "voids"

    def __str__(self) -> str:
        return str(self.value)
