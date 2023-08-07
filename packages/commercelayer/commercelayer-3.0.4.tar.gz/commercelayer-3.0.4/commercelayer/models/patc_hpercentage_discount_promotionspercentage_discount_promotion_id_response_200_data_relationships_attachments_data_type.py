from enum import Enum


class PATCHpercentageDiscountPromotionspercentageDiscountPromotionIdResponse200DataRelationshipsAttachmentsDataType(
    str, Enum
):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
