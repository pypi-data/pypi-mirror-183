from enum import Enum


class GETparcelsparcelIdResponse200DataRelationshipsEventsDataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
