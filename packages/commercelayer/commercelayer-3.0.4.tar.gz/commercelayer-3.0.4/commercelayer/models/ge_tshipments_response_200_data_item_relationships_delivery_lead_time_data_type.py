from enum import Enum


class GETshipmentsResponse200DataItemRelationshipsDeliveryLeadTimeDataType(str, Enum):
    DELIVERY_LEAD_TIME = "delivery_lead_time"

    def __str__(self) -> str:
        return str(self.value)
