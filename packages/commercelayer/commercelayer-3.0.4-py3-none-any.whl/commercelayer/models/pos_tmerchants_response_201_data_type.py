from enum import Enum


class POSTmerchantsResponse201DataType(str, Enum):
    MERCHANTS = "merchants"

    def __str__(self) -> str:
        return str(self.value)
