from enum import Enum


class GETwebhooksResponse200DataItemRelationshipsLastEventCallbacksDataType(str, Enum):
    LAST_EVENT_CALLBACKS = "last_event_callbacks"

    def __str__(self) -> str:
        return str(self.value)
