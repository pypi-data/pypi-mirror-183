from enum import Enum


class OrderDataRelationshipsVoidsDataType(str, Enum):
    VOIDS = "voids"

    def __str__(self) -> str:
        return str(self.value)
