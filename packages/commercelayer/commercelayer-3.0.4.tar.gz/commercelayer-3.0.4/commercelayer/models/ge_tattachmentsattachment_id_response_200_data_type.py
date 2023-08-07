from enum import Enum


class GETattachmentsattachmentIdResponse200DataType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
