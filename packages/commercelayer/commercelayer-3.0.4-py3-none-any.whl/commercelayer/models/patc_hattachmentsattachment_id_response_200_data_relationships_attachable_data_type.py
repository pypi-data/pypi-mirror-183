from enum import Enum


class PATCHattachmentsattachmentIdResponse200DataRelationshipsAttachableDataType(str, Enum):
    ATTACHABLE = "attachable"

    def __str__(self) -> str:
        return str(self.value)
