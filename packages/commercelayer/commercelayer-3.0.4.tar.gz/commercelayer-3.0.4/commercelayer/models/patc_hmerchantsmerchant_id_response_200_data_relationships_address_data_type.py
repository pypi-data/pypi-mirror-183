from enum import Enum


class PATCHmerchantsmerchantIdResponse200DataRelationshipsAddressDataType(str, Enum):
    ADDRESS = "address"

    def __str__(self) -> str:
        return str(self.value)
