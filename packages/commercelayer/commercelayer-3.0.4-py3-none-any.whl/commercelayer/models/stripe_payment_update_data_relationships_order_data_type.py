from enum import Enum


class StripePaymentUpdateDataRelationshipsOrderDataType(str, Enum):
    ORDERS = "orders"

    def __str__(self) -> str:
        return str(self.value)
