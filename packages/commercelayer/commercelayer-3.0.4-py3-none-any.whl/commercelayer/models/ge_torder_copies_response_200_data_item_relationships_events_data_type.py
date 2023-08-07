from enum import Enum


class GETorderCopiesResponse200DataItemRelationshipsEventsDataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
