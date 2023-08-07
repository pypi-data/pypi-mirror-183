from enum import Enum


class PATCHordersorderIdResponse200DataRelationshipsVoidsDataType(str, Enum):
    VOIDS = "voids"

    def __str__(self) -> str:
        return str(self.value)
