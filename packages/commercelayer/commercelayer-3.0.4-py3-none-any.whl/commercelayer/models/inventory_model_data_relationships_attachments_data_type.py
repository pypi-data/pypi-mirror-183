from enum import Enum


class InventoryModelDataRelationshipsAttachmentsDataType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
