from enum import Enum


class GETmerchantsResponse200DataItemType(str, Enum):
    MERCHANTS = "merchants"

    def __str__(self) -> str:
        return str(self.value)
