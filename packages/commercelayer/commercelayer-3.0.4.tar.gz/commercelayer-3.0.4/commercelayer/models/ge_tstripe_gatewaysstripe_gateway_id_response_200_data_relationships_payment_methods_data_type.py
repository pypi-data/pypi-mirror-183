from enum import Enum


class GETstripeGatewaysstripeGatewayIdResponse200DataRelationshipsPaymentMethodsDataType(str, Enum):
    PAYMENT_METHODS = "payment_methods"

    def __str__(self) -> str:
        return str(self.value)
