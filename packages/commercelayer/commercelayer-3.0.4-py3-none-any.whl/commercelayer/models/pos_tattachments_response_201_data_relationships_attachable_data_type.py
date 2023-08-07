from enum import Enum


class POSTattachmentsResponse201DataRelationshipsAttachableDataType(str, Enum):
    ATTACHABLE = "attachable"

    def __str__(self) -> str:
        return str(self.value)
