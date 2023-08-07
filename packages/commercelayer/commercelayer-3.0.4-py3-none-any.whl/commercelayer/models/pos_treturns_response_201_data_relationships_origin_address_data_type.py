from enum import Enum


class POSTreturnsResponse201DataRelationshipsOriginAddressDataType(str, Enum):
    ORIGIN_ADDRESS = "origin_address"

    def __str__(self) -> str:
        return str(self.value)
