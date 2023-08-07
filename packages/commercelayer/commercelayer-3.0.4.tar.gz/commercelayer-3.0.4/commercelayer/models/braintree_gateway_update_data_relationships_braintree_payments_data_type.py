from enum import Enum


class BraintreeGatewayUpdateDataRelationshipsBraintreePaymentsDataType(str, Enum):
    BRAINTREE_PAYMENTS = "braintree_payments"

    def __str__(self) -> str:
        return str(self.value)
