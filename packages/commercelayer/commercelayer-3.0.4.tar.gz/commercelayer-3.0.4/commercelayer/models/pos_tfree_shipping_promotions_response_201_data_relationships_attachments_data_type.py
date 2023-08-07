from enum import Enum


class POSTfreeShippingPromotionsResponse201DataRelationshipsAttachmentsDataType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
