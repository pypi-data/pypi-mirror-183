from enum import Enum


class GETeventsResponse200DataItemType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
