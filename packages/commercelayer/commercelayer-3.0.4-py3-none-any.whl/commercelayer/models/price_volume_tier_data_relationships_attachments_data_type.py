from enum import Enum


class PriceVolumeTierDataRelationshipsAttachmentsDataType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
