from enum import Enum


class PATCHshipmentsshipmentIdResponse200DataRelationshipsAvailableShippingMethodsDataType(str, Enum):
    AVAILABLE_SHIPPING_METHODS = "available_shipping_methods"

    def __str__(self) -> str:
        return str(self.value)
