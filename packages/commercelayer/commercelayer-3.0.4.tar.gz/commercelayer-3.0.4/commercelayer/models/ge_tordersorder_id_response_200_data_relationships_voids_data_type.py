from enum import Enum


class GETordersorderIdResponse200DataRelationshipsVoidsDataType(str, Enum):
    VOIDS = "voids"

    def __str__(self) -> str:
        return str(self.value)
