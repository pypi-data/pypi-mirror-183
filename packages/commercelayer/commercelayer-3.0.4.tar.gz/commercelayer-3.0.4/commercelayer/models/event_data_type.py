from enum import Enum


class EventDataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
