from enum import Enum


class POSTmerchantsResponse201DataRelationshipsAddressDataType(str, Enum):
    ADDRESS = "address"

    def __str__(self) -> str:
        return str(self.value)
