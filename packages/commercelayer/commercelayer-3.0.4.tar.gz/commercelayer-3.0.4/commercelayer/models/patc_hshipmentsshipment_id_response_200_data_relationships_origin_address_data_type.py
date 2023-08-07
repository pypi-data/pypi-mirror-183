from enum import Enum


class PATCHshipmentsshipmentIdResponse200DataRelationshipsOriginAddressDataType(str, Enum):
    ORIGIN_ADDRESS = "origin_address"

    def __str__(self) -> str:
        return str(self.value)
