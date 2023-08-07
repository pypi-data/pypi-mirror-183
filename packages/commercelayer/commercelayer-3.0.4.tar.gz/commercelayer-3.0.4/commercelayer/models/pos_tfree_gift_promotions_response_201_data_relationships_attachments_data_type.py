from enum import Enum


class POSTfreeGiftPromotionsResponse201DataRelationshipsAttachmentsDataType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
