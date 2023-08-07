from enum import Enum


class GETshipmentsResponse200DataItemRelationshipsAvailableShippingMethodsDataType(str, Enum):
    AVAILABLE_SHIPPING_METHODS = "available_shipping_methods"

    def __str__(self) -> str:
        return str(self.value)
