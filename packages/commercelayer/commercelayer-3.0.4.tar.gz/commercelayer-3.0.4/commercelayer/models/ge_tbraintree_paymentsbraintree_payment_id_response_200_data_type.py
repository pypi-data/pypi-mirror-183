from enum import Enum


class GETbraintreePaymentsbraintreePaymentIdResponse200DataType(str, Enum):
    BRAINTREE_PAYMENTS = "braintree_payments"

    def __str__(self) -> str:
        return str(self.value)
