from enum import Enum


class GETeventCallbacksResponse200DataItemType(str, Enum):
    EVENT_CALLBACKS = "event_callbacks"

    def __str__(self) -> str:
        return str(self.value)
