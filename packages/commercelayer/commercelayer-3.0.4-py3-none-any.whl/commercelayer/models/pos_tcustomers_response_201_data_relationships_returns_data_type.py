from enum import Enum


class POSTcustomersResponse201DataRelationshipsReturnsDataType(str, Enum):
    RETURNS = "returns"

    def __str__(self) -> str:
        return str(self.value)
