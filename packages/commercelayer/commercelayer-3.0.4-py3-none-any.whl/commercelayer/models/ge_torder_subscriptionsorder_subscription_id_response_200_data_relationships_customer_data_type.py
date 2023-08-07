from enum import Enum


class GETorderSubscriptionsorderSubscriptionIdResponse200DataRelationshipsCustomerDataType(str, Enum):
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return str(self.value)
