from enum import Enum


class GETcustomerSubscriptionscustomerSubscriptionIdResponse200DataRelationshipsCustomerDataType(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
