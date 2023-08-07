from enum import Enum


class PATCHstockLocationsstockLocationIdResponse200DataRelationshipsAddressDataType(str, Enum):
    ADDRESS = "address"

    def __str__(self) -> str:
        return str(self.value)
