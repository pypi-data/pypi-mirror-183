from enum import Enum


class GETmerchantsmerchantIdResponse200DataType(str, Enum):
    MERCHANTS = "merchants"

    def __str__(self) -> str:
        return str(self.value)
