from enum import Enum


class POSTdeliveryLeadTimesResponse201DataRelationshipsShippingMethodDataType(str, Enum):
    SHIPPING_METHOD = "shipping_method"

    def __str__(self) -> str:
        return str(self.value)
