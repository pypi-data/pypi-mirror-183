from enum import Enum


class PATCHadyenPaymentsadyenPaymentIdResponse200DataType(str, Enum):
    ADYEN_PAYMENTS = "adyen_payments"

    def __str__(self) -> str:
        return str(self.value)
