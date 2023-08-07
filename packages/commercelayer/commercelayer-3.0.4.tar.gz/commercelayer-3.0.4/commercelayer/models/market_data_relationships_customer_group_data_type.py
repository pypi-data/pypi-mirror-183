from enum import Enum


class MarketDataRelationshipsCustomerGroupDataType(str, Enum):
    CUSTOMER_GROUPS = "customer_groups"

    def __str__(self) -> str:
        return str(self.value)
