from enum import Enum


class POSTorderCopiesResponse201DataRelationshipsEventsDataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
