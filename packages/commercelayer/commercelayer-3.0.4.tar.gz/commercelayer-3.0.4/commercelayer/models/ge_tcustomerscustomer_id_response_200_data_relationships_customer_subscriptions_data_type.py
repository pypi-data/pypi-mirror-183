from enum import Enum


class GETcustomerscustomerIdResponse200DataRelationshipsCustomerSubscriptionsDataType(str, Enum):
    CUSTOMER_SUBSCRIPTIONS = "customer_subscriptions"

    def __str__(self) -> str:
        return str(self.value)
