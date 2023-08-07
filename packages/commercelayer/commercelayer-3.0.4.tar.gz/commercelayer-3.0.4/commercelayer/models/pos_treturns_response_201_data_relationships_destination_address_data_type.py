from enum import Enum


class POSTreturnsResponse201DataRelationshipsDestinationAddressDataType(str, Enum):
    DESTINATION_ADDRESS = "destination_address"

    def __str__(self) -> str:
        return str(self.value)
