from enum import Enum


class GETmerchantsmerchantIdResponse200DataRelationshipsAddressDataType(str, Enum):
    ADDRESS = "address"

    def __str__(self) -> str:
        return str(self.value)
