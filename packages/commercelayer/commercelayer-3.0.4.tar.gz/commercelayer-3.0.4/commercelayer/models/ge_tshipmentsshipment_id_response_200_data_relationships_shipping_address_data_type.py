from enum import Enum


class GETshipmentsshipmentIdResponse200DataRelationshipsShippingAddressDataType(str, Enum):
    SHIPPING_ADDRESS = "shipping_address"

    def __str__(self) -> str:
        return str(self.value)
