from enum import Enum


class PATCHreturnsreturnIdResponse200DataRelationshipsEventsDataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
