from enum import Enum


class POSTcustomerAddressesResponse201DataRelationshipsEventsDataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
