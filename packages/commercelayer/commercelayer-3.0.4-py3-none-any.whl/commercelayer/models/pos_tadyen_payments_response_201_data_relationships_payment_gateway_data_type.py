from enum import Enum


class POSTadyenPaymentsResponse201DataRelationshipsPaymentGatewayDataType(str, Enum):
    PAYMENT_GATEWAY = "payment_gateway"

    def __str__(self) -> str:
        return str(self.value)
