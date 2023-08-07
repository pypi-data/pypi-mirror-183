from enum import Enum


class POSTwebhooksResponse201DataType(str, Enum):
    WEBHOOKS = "webhooks"

    def __str__(self) -> str:
        return str(self.value)
