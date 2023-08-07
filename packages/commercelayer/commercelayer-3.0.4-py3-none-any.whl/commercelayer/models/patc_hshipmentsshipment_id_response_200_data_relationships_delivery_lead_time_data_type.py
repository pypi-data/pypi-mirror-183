from enum import Enum


class PATCHshipmentsshipmentIdResponse200DataRelationshipsDeliveryLeadTimeDataType(str, Enum):
    DELIVERY_LEAD_TIME = "delivery_lead_time"

    def __str__(self) -> str:
        return str(self.value)
