from enum import Enum


class GETcleanupsResponse200DataItemRelationshipsEventsDataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
