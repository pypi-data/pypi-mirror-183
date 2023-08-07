from enum import Enum


class PATCHorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsEventsDataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
