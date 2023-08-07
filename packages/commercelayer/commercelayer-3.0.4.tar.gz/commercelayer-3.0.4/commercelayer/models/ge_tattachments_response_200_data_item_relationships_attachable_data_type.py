from enum import Enum


class GETattachmentsResponse200DataItemRelationshipsAttachableDataType(str, Enum):
    ATTACHABLE = "attachable"

    def __str__(self) -> str:
        return str(self.value)
