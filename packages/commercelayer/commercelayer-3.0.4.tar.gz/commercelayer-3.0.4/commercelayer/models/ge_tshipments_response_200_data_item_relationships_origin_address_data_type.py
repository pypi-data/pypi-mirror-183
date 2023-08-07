from enum import Enum


class GETshipmentsResponse200DataItemRelationshipsOriginAddressDataType(str, Enum):
    ORIGIN_ADDRESS = "origin_address"

    def __str__(self) -> str:
        return str(self.value)
