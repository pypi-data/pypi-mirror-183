from enum import Enum


class GETattachmentsResponse200DataItemType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
