from enum import Enum


class PATCHpaypalGatewayspaypalGatewayIdResponse200DataRelationshipsPaypalPaymentsDataType(str, Enum):
    PAYPAL_PAYMENTS = "paypal_payments"

    def __str__(self) -> str:
        return str(self.value)
