from enum import Enum


class GETstockTransfersResponse200DataItemRelationshipsEventsDataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
