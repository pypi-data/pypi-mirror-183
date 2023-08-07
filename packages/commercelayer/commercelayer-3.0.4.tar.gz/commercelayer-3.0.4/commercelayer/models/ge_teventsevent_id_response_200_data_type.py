from enum import Enum


class GETeventseventIdResponse200DataType(str, Enum):
    EVENTS = "events"

    def __str__(self) -> str:
        return str(self.value)
