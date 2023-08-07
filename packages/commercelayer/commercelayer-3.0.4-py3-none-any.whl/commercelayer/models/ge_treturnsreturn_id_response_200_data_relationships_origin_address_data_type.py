from enum import Enum


class GETreturnsreturnIdResponse200DataRelationshipsOriginAddressDataType(str, Enum):
    ORIGIN_ADDRESS = "origin_address"

    def __str__(self) -> str:
        return str(self.value)
