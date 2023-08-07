from enum import Enum


class PATCHattachmentsattachmentIdResponse200DataType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
