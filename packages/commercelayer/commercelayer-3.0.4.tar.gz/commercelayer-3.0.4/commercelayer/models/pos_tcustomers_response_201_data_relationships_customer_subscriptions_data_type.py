from enum import Enum


class POSTcustomersResponse201DataRelationshipsCustomerSubscriptionsDataType(str, Enum):
    CUSTOMER_SUBSCRIPTIONS = "customer_subscriptions"

    def __str__(self) -> str:
        return str(self.value)
