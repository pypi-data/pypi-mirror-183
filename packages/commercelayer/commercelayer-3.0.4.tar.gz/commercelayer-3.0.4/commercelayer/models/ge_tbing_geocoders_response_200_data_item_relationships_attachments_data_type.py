from enum import Enum


class GETbingGeocodersResponse200DataItemRelationshipsAttachmentsDataType(str, Enum):
    ATTACHMENTS = "attachments"

    def __str__(self) -> str:
        return str(self.value)
