from enum import Enum


class GETshippingWeightTiersshippingWeightTierIdResponse200DataRelationshipsAttachmentsDataType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
