from enum import Enum


class POSTattachmentsResponse201DataType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
